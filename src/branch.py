import copy 
from utils import numeric_to_valid_str, is_str_true

class Branch:
    def __init__(self):
        self.init_line = "/BRANCH\n"
        self.comment_line_type_0 = "C < n1 >< n2 ><ref1><ref2>< R  >< L  >< C  >\n"
        self.comment_line_distrib_params = "C < n1 >< n2 ><ref1><ref2>< R  >< A  >< B  ><Leng><><>0\n"

        self.branches = []

    def write(self):
        return self.init_line + self.comment_line_type_0 + self.comment_line_distrib_params + "".join([branch.write() for branch in self.branches])
    
    def add_branch(self, branch):
        if not isinstance(branch, RlcElement):
            raise TypeError("Branch must be of type RlcElement")
        self.branches.append(branch)

    def copy(self):
        return copy.deepcopy(self)
    
    def from_file(self, filename): 
        with open(filename, "r") as f:
            lines = f.readlines()

        first_line_index = -1
        last_line_index = -1

        for index, line in enumerate(lines):
            if line.startswith("/BRANCH"):
                first_line_index = index + 1
                break

        
        # Start looking for the last line after the first line
        for index, line in enumerate(lines[first_line_index:]):
            if line.startswith("/"):
                last_line_index = index + first_line_index
                break



        lines = [line for line in lines[first_line_index:last_line_index] if not line.startswith("C")]

        lines = [line[:-1] for line in lines]


        for line in lines:
            if line.startswith(" "): 
                rlc_basic = RlcElementBasic()
                rlc_basic.line = line
                self.add_branch(rlc_basic)
            else:
                rlc_distrib = RlcElementDistParams()
                rlc_distrib.line = line
                self.add_branch(rlc_distrib)

        return self

class RlcElement:
    def __init__(self):
        itype_str_len = 2
        self._itype = " " * itype_str_len

        node_str_len = 6
        self._node_1 = " " * node_str_len
        self._node_2 = " " * node_str_len
        self._node_ref_1  = " " * node_str_len
        self._node_ref_2  = " " * node_str_len

        resistance_str_len = 6

        self._resistance = " " * resistance_str_len

    def copy(self):
        return copy.deepcopy(self)

class RlcElementBasic(RlcElement):
    def __init__(self):
        super().__init__()

        line_len = 80
        self._line = " " * line_len

        inductance_capacitance_str_len = 6

        self._inductance = " " * inductance_capacitance_str_len
        self._capacitance = " " * inductance_capacitance_str_len
        self._iout = " "

        blank_len = 35
        self._blank = " " * blank_len

    def write(self):
        return f"{self.line}\n"
    
    @property
    def itype(self):
        return self._itype
    
    @itype.setter
    def itype(self, new_itype):
        if len(new_itype) > 2:
            raise ValueError("Itype cannot be longer than 2 characters")
        
        self._line = new_itype.ljust(2) + self._line[2:]
        self._itype = new_itype.ljust(2)

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) > 6:
            raise ValueError("Node 1 cannot be longer than 6 characters")
        
        self._line = new_node_1.ljust(6) + self._line[6:]

        self._node_1 = new_node_1.ljust(6)
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) > 6:
            raise ValueError("Node 2 cannot be longer than 6 characters")
        
        self._line = self._line[0:8] + new_node_2.ljust(6) + self._line[14:]

        self._node_2 = new_node_2.ljust(6)
    
    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter
    def node_ref_1(self, new_node_ref_1):
        if len(new_node_ref_1) > 6:
            raise ValueError("Node ref 1 cannot be longer than 6 characters")
        
        self._line = self._line[0:14] + new_node_ref_1.ljust(6) + self._line[20:]

        self._node_ref_1 = new_node_ref_1.ljust(6)

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter
    def node_ref_2(self, new_node_ref_2):
        if len(new_node_ref_2) > 6:
            raise ValueError("Node ref 2 cannot be longer than 6 characters")
        
        self._line = self._line[0:20] + new_node_ref_2.ljust(6) + self._line[26:]

        self._node_ref_2 = new_node_ref_2.ljust(6)
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, new_resistance):

        if new_resistance != " " * 6:
            try:
                float(new_resistance)
            except ValueError:
                raise ValueError("Resistance must be a numeric value")

        new_resistance = numeric_to_valid_str(new_resistance)



        if len(new_resistance) > 6:
            raise ValueError("Resistance cannot be longer than 6 characters")
        
        self._line = self._line[0:26] + new_resistance.ljust(6) + self._line[32:]

        self._resistance = new_resistance.ljust(6)
    
    @property
    def inductance(self):
        return self._inductance
    
    @inductance.setter
    def inductance(self, new_inductance):

        if new_inductance != " " * 6:
            try:
                float(new_inductance)
            except ValueError:
                raise ValueError("Inductance must be a numeric value")
        
        new_inductance = numeric_to_valid_str(
            new_inductance, 
            is_inductance=(not is_str_true(self.miscellaneous.x_opt))
        )

        if len(new_inductance) > 6:
            raise ValueError("Inductance cannot be longer than 6 characters")
        
        self._line = self._line[0:32] + new_inductance.ljust(6) + self._line[38:]

        self._inductance = new_inductance.ljust(6)
    
    @property
    def capacitance(self):
        return self._capacitance
    
    @capacitance.setter
    def capacitance(self, new_capacitance):

        if new_capacitance != " " * 6:
            try:
                float(new_capacitance)
            except ValueError:
                raise ValueError("Capacitance must be a numeric value")
            
        new_capacitance = numeric_to_valid_str(new_capacitance, is_capacitance=True)

        if len(new_capacitance) > 6:
            raise ValueError("Capacitance cannot be longer than 6 characters")
        
        self._line = self._line[0:38] + new_capacitance.ljust(6) + self._line[44:]
        
        self._capacitance = new_capacitance.ljust(6)
    
    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) > 1:
            raise ValueError("Iout cannot be longer than 1 character")
        
        self._line = self._line[0:79] + new_iout

        self._iout = new_iout.ljust(1)

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than be 80 characters long")
        
        self._line = new_line.ljust(80)

        self._itype = new_line[0:2]
        self._node_1 = new_line[2:8]
        self._node_2 = new_line[8:14]
        self._node_ref_1 = new_line[14:20]
        self._node_ref_2 = new_line[20:26]
        self._resistance = new_line[26:32]
        self._inductance = new_line[32:38]
        self._capacitance = new_line[38:44]
        self._iout = new_line[79]

class RlcElementDistParams(RlcElement):
    def __init__(self):
        super().__init__()

        line_len = 80
        self._line = " " * line_len

        type_len = 2
        self._itype = " " * type_len

        iline_len = 2
        self._iline = " " * iline_len

        ipunch_len = 2
        self._ipunch = " " * ipunch_len

        ipose_len = 2
        self._ipose = " " * ipose_len

        param_len = 6
        self._distribution_param_a = " " * param_len
        self._distribution_param_b = " " * param_len

        length_len = 6
        self._length = " " * length_len

        blank_len = 23
        self._blank = " " * blank_len

        self._iout = " "


        
    

    def write(self):
        return f"{self.line}\n"
    
    @property
    def itype(self):
        return self._itype
    
    @itype.setter
    def itype(self, new_itype):
        if len(new_itype) > 2:
            raise ValueError("Itype cannot be longer than 2 characters long")
        
        self._line = new_itype.ljust(2) + self._line[2:]

        self._itype = new_itype.ljust(2)

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) > 6:
            raise ValueError("Node cannot be longer than be 6 characters long")
        
        self._line = self._line[0:2] + new_node_1.ljust(6) + self._line[8:]

        self._node_1 = new_node_1.ljust(6)
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) > 6:
            raise ValueError("Node cannot be longer than be 6 characters long")
        
        self._line = self._line[0:8] + new_node_2.ljust(6) + self._line[14:]

        self._node_2 = new_node_2.ljust(6)

    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter
    def node_ref_1(self, new_node_ref_1):
        if len(new_node_ref_1) > 6:
            raise ValueError("Node cannot be longer than be 6 characters long")
        
        self._line = self._line[0:14] + new_node_ref_1.ljust(6) + self._line[20:]

        self._node_ref_1 = new_node_ref_1.ljust(6)

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter
    def node_ref_2(self, new_node_ref_2):
        if len(new_node_ref_2) > 6:
            raise ValueError("Node cannot be longer than be 6 characters long")
        
        self._line = self._line[0:20] + new_node_ref_2.ljust(6) + self._line[26:]

        self._node_ref_2 = new_node_ref_2.ljust(6)
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, new_resistance):
        if len(new_resistance) > 6:
            raise ValueError("Resistance cannot be longer than 6 characters long")
        
        self._line = self._line[0:26] + new_resistance.ljust(6) + self._line[32:]

        self._resistance = new_resistance.ljust(6)
    
    @property
    def distribution_param_a(self):
        return self._distribution_param_a
    
    @distribution_param_a.setter
    def distribution_param_a(self, new_distribution_param_a):
        if len(new_distribution_param_a) > 6:
            raise ValueError("Distribution cannot be longer than be 6 characters long")
        
        self._line = self._line[0:32] + new_distribution_param_a.ljust(6) + self._line[38:]
        self._distribution_param_a = new_distribution_param_a.ljust(6)
    
    @property
    def distribution_param_b(self):
        return self._distribution_param_b
    
    @distribution_param_b.setter
    def distribution_param_b(self, new_distribution_param_b):
        if len(new_distribution_param_b) > 6:
            raise ValueError("Distribution cannot be longer than be 6 characters long")
        
        self._line = self._line[0:38] + new_distribution_param_b.ljust(6) + self._line[44:]

        self._distribution_param_b = new_distribution_param_b.ljust(6)
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_length):
        if len(new_length) > 6:
            raise ValueError("Length cannot be longer than 6 characters long")
        
        self._line = self._line[0:44] + new_length.ljust(6) + self._line[50:]

        self._length = new_length.ljust(6)

    @property
    def iline(self):
        return self._iline

    @iline.setter
    def iline(self, new_iline):
        if len(new_iline) > 2:
            raise ValueError("Iline cannot be longer than 2 characters long")
        
        self._line = self._line[0:50] + new_iline.ljust(2) + self._line[52:]
        self._iline = new_iline.ljust(2)

    @property
    def ipunch(self):
        return self._ipunch
    
    @ipunch.setter
    def ipunch(self, new_ipunch):
        if len(new_ipunch) > 2:
            raise ValueError("Ipunch cannot be longer than 2 characters long")
        
        self._line = self._line[0:52] + new_ipunch.ljust(2) + self._line[54:]
        self._ipunch = new_ipunch.ljust(2)
    
    @property
    def ipose(self):
        return self._ipose
    
    @ipose.setter
    def ipose(self, new_ipose):
        if len(new_ipose) > 2:
            raise ValueError("Ipose cannot be longer than 2 characters long")
        
        self._line = self._line[0:54] + new_ipose.ljust(2) + self._line[56:]
        self._ipose = new_ipose.ljust(2)
    
    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) > 1:
            raise ValueError("Iout cannot be longer than 1 characters long")
        
        self._line = self._line[0:79] + new_iout
        self._iout = new_iout.ljust(1)
