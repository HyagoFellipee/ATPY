import copy 
from utils import numeric_to_valid_str, is_str_true, cant_be_longer_message, valid_iout

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

        spot_len = 2

        if len(new_itype) > spot_len:
            raise ValueError(cant_be_longer_message('new_itype', spot_len))
        
        self._line = new_itype.ljust(spot_len) + self._line[spot_len:]
        self._itype = new_itype.ljust(spot_len)

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter
    def node_1(self, new_node_1):
        
        spot_len = 6
        init_index = 2
        end_index = 8
        
        if len(new_node_1) > spot_len:
            raise ValueError(cant_be_longer_message('new_node_1', spot_len))
        
        self._line = self._line[0:init_index] + new_node_1.ljust(spot_len) + self._line[end_index:]

        self._node_1 = new_node_1.ljust(spot_len)
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter     
    def node_2(self, new_node_2):
        
        spot_len = 6
        init_index = 8
        end_index = 14
        
        if len(new_node_2) > spot_len:
            raise ValueError(cant_be_longer_message('new_node_2', spot_len))
        
        self._line = self._line[0:init_index] + new_node_2.ljust(spot_len) + self._line[end_index:]

        self._node_2 = new_node_2.ljust(spot_len)
    
    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter     
    def node_ref_1(self, new_node_ref_1):
        
        spot_len = 6
        init_index = 14
        end_index = 20
        
        if len(new_node_ref_1) > spot_len:
            raise ValueError(cant_be_longer_message('new_node_ref_1', spot_len))
        
        self._line = self._line[0:init_index] + new_node_ref_1.ljust(spot_len) + self._line[end_index:]

        self._node_ref_1 = new_node_ref_1.ljust(spot_len)

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter     
    def node_ref_2(self, new_node_ref_2):
        
        spot_len = 6
        init_index = 20
        end_index = 26
        
        if len(new_node_ref_2) > spot_len:
            raise ValueError(cant_be_longer_message('new_node_ref_2', spot_len))
        
        self._line = self._line[0:init_index] + new_node_ref_2.ljust(spot_len) + self._line[end_index:]

        self._node_ref_2 = new_node_ref_2.ljust(spot_len)
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, new_resistance):

        spot_len = 6
        init_index = 26
        end_index = 32

        if new_resistance != " " * 6:
            try:
                float(new_resistance)
            except ValueError:
                raise ValueError("Resistance must be a numeric value")

        new_resistance = numeric_to_valid_str(new_resistance, spot_len)
    
        if len(new_resistance) > spot_len:
            raise ValueError(cant_be_longer_message('new_resistance', spot_len))
        
        self._line = self._line[0:init_index] + new_resistance.ljust(spot_len) + self._line[end_index:]

        self._resistance = new_resistance.ljust(spot_len)
    
    @property
    def inductance(self):
        return self._inductance
    
    @inductance.setter
    def inductance(self, new_inductance):
             
        spot_len = 6
        init_index = 32
        end_index = 38
        
        if new_inductance != " ".ljust(spot_len):
            try:
                float(new_inductance)
            except ValueError:
                raise ValueError("Inductance must be a numeric value")
        
        new_inductance = numeric_to_valid_str(
            new_inductance, 
            spot_len, 
            is_inductance=(not is_str_true(self.miscellaneous.x_opt)) # if x_opt is true, then inductance unit is ohm, as in impedance
        ) 

        if len(new_inductance) > spot_len:
            raise ValueError(cant_be_longer_message('new_inductance', spot_len))
        
        self._line = self._line[0:init_index] + new_inductance.ljust(spot_len) + self._line[end_index:]

        self._inductance = new_inductance.ljust(spot_len)
    
    @property
    def capacitance(self):
        return self._capacitance
    
    @capacitance.setter
    def capacitance(self, new_capacitance):

        spot_len = 6
        init_index = 38
        end_index = 44

        if new_capacitance != " ".ljust(spot_len):
            try:
                float(new_capacitance)
            except ValueError:
                raise ValueError("Capacitance must be a numeric value")
            
        new_capacitance = numeric_to_valid_str(new_capacitance, spot_len, is_capacitance=True)
        
        if len(new_capacitance) > spot_len:
            raise ValueError(cant_be_longer_message('new_capacitance', spot_len))
        
        self._line = self._line[0:init_index] + new_capacitance.ljust(spot_len) + self._line[end_index:]
        
        self._capacitance = new_capacitance.ljust(spot_len)
    
    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):

        spot_len = 1
        init_index = 79

        new_iout = valid_iout(new_iout, spot_len)
        new_iout = numeric_to_valid_str(new_iout, spot_len) if new_iout != 0 else " " * spot_len

        if len(new_iout) > spot_len:
            raise ValueError(cant_be_longer_message("new_iout", spot_len))
        
        self._line = self._line[0:init_index] + new_iout

        self._iout = new_iout.ljust(spot_len)

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):

        if len(new_line) > self.line_len:
            raise ValueError(cant_be_longer_message("new_line", self.line_len))
        
        self._line = new_line.ljust(self.line_len)

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

        spot_len = 2


        if len(new_itype) > spot_len:
            raise ValueError(cant_be_longer_message("new_itype", spot_len))
        
        self._line = new_itype.ljust(spot_len) + self._line[2:]

        self._itype = new_itype.ljust(spot_len)

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter     
    def node_1(self, new_node_1):
        
        spot_len = 6
        init_index = 2
        end_index = 8
        
        if len(new_node_1) > spot_len:
            raise ValueError(cant_be_longer_message(new_node_1, spot_len))
        
        self._line = self._line[0:init_index] + new_node_1.ljust(spot_len) + self._line[end_index:]

        self._node_1 = new_node_1.ljust(spot_len)
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter     
    def node_2(self, new_node_2):
        
        spot_len = 6
        init_index = 8
        end_index = 14
        
        if len(new_node_2) > spot_len:
            raise ValueError(cant_be_longer_message(new_node_2, spot_len))
        
        self._line = self._line[0:init_index] + new_node_2.ljust(spot_len) + self._line[end_index:]

        self._node_2 = new_node_2.ljust(spot_len)

    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter     
    def node_ref_1(self, new_node_ref_1):
        
        spot_len = 6
        init_index = 14
        end_index = 20
        
        if len(new_node_ref_1) > spot_len:
            raise ValueError(cant_be_longer_message(new_node_ref_1, spot_len))
        
        self._line = self._line[0:init_index] + new_node_ref_1.ljust(spot_len) + self._line[end_index:]

        self._node_ref_1 = new_node_ref_1.ljust(spot_len)

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter     
    def node_ref_2(self, new_node_ref_2):
        
        spot_len = 6
        init_index = 20
        end_index = 26
        
        if len(new_node_ref_2) > spot_len:
            raise ValueError(cant_be_longer_message(new_node_ref_2, spot_len))
        
        self._line = self._line[0:init_index] + new_node_ref_2.ljust(spot_len) + self._line[end_index:]

        self._node_ref_2 = new_node_ref_2.ljust(spot_len)
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter     
    def resistance(self, new_resistance):
        
        spot_len = 6
        init_index = 26
        end_index = 32
        
        if len(new_resistance) > spot_len:
            raise ValueError(cant_be_longer_message(new_resistance, spot_len))
        
        self._line = self._line[0:init_index] + new_resistance.ljust(spot_len) + self._line[end_index:]

        self._resistance = new_resistance.ljust(spot_len)
    
    @property
    def distribution_param_a(self):
        return self._distribution_param_a
    
    @distribution_param_a.setter       
    def distribution_param_a(self, new_distribution_param_a):
        
        spot_len = 6
        init_index = 32
        end_index = 38

        if len(new_distribution_param_a) > spot_len:
            raise ValueError(cant_be_longer_message(new_distribution_param_a, spot_len))
        
        self._line = self._line[0:init_index] + new_distribution_param_a.ljust(spot_len) + self._line[end_index:]
        self._distribution_param_a = new_distribution_param_a.ljust(spot_len)
    
    @property
    def distribution_param_b(self):
        return self._distribution_param_b
    
    @distribution_param_b.setter       
    def distribution_param_b(self, new_distribution_param_b):
        
        spot_len = 6
        init_index = 38
        end_index = 44
        
        if len(new_distribution_param_b) > spot_len:
            raise ValueError(cant_be_longer_message(new_distribution_param_b, spot_len))
        
        self._line = self._line[0:init_index] + new_distribution_param_b.ljust(spot_len) + self._line[end_index:]

        self._distribution_param_b = new_distribution_param_b.ljust(spot_len)
    
    @property
    def length(self):
        return self._length
    
    @length.setter     
    def length(self, new_length):
        
        spot_len = 6
        init_index = 44
        end_index = 50
        
        if len(new_length) > spot_len:
            raise ValueError(cant_be_longer_message(new_length, spot_len))
        
        self._line = self._line[0:init_index] + new_length.ljust(spot_len) + self._line[end_index:]

        self._length = new_length.ljust(spot_len)

    @property
    def iline(self):
        return self._iline

    @iline.setter
    def iline(self, new_iline):

        spot_len = 2
        init_index = 50
        end_index = 52

        if len(new_iline) > spot_len:
            raise ValueError(cant_be_longer_message("new_iline", spot_len))
        
        self._line = self._line[0:init_index] + new_iline.ljust(spot_len) + self._line[end_index:]
        self._iline = new_iline.ljust(spot_len)

    @property
    def ipunch(self):
        return self._ipunch
    
    @ipunch.setter
    def ipunch(self, new_ipunch):
    
        spot_len = 2
        init_index = 52
        end_index = 54

        if len(new_ipunch) > spot_len:
            raise ValueError(cant_be_longer_message(new_ipunch, spot_len))
        
        self._line = self._line[0:init_index] + new_ipunch.ljust(spot_len) + self._line[end_index:]
        self._ipunch = new_ipunch.ljust(spot_len)
    
    @property
    def ipose(self):
        return self._ipose
    
    @ipose.setter
    def ipose(self, new_ipose):

        spot_len = 2    
        init_index = 54
        end_index = 56

        if len(new_ipose) > spot_len:
            raise ValueError(cant_be_longer_message("new_ipose", spot_len))
        
        self._line = self._line[0:init_index] + new_ipose.ljust(spot_len) + self._line[end_index:]
        self._ipose = new_ipose.ljust(spot_len)
    
    @property
    def iout(self):
        return self._iout
    @iout.setter
    def iout(self, new_iout):

        spot_len = 1 
        init_index = 79

        new_iout = valid_iout(new_iout, spot_len)
        new_iout = numeric_to_valid_str(new_iout, spot_len) if new_iout != 0 else " " * spot_len

        if len(new_iout) > 1:
            raise ValueError(cant_be_longer_message("new_iout", spot_len)) 
        
        self._line = self._line[0:init_index] + new_iout
        self._iout = new_iout.ljust(spot_len)
