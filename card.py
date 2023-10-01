class ATPCard: 
    def __init__(self) -> None:
        self.miscellaneous = Miscellaneous()
        self.models = Models() 
        self.branch = Branch() 
        self.switch = Switch()
        self.source = Source()
        self.output = Output()
        self.plot = Plot()

        self.high_precison = False 
        self.fixed_format = True 
        self.exact_phasor = False


    def write(self):
        card_str = ""

        init_line = "BEGIN NEW DATA CASE\n"
        numbering_line = "C        1         2         3         4         5         6         7         8\nC 345678901234567890123456789012345678901234567890123456789012345678901234567890\n"

        end_line = "BLANK BRANCH\nBLANK SWITCH\nBLANK SOURCE\nBLANK OUTPUT\nBLANK PLOT\nBEGIN NEW DATA CASE\nBLANK"

        card_str += init_line
        if self.exact_phasor:
            card_str += "EXACT PHASOR EQUIVALENT\n"

        card_str += self.miscellaneous.write()
        card_str += numbering_line
        # card_str += self.models.write()
        card_str += self.branch.write()
        card_str += self.switch.write()
        # card_str += self.source.write()
        card_str += self.output.write()
        # card_str += self.plot.write()

        card_str += end_line

        return card_str

    def write_to_file(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.write())


class Miscellaneous:
    def __init__(self) -> None:

        self.comment_line = "C  dT  >< Tmax >< Xopt >< Copt ><Epsiln>"


        self._first_line =  "   1.E-6    .001                                        " 
        self._second_line = "     500       1       1       1       1       0       0       1       0        " 

        # First Miscellaneous line 
        self._delta_t = "   1.E-6"
        self._t_max   = "    .001"
        self._x_opt   = "        "  
        self._c_opt   = "        "  
        self._epslin  = "        "  
        self._tolmat  = "        "  
        self._tstart  = "        "  


        # Second Miscellaneous line
        self._iout   = "     500"
        self._iplot  = "       1"
        self._idoubl = "       1"
        self._kout   = "       1"
        self._maxout = "       1"
        self._ipun   = "       0"
        self._memsav = "       0"
        self._icat   = "       1"
        self._nenerg = "       0"
        self._iprsup = "        "


    @property
    def delta_t(self):
        return self._delta_t
    
    @delta_t.setter
    def delta_t(self, new_delta_t):
        if len(new_delta_t) != 8:
            raise ValueError("Delta t must be 8 characters long")
        

        self.first_line = new_delta_t + self.first_line[8:]
        

        self._delta_t = new_delta_t

    @property
    def t_max(self):
        return self._t_max
    
    @t_max.setter
    def t_max(self, new_t_max):
        if len(new_t_max) != 8:
            raise ValueError("T max must be 8 characters long")
        
        self.first_line = self.first_line[0:8] + new_t_max + self.first_line[16:]

        self._t_max = new_t_max

    @property
    def x_opt(self):
        return self._x_opt
    
    @x_opt.setter
    def x_opt(self, new_x_opt):
        if len(new_x_opt) != 8:
            raise ValueError("X opt must be 8 characters long")
        
        self.first_line = self.first_line[0:16] + new_x_opt + self.first_line[24:]

        self._x_opt = new_x_opt
    
    @property
    def c_opt(self):
        return self._c_opt
    
    @c_opt.setter
    def c_opt(self, new_c_opt):
        if len(new_c_opt) != 8:
            raise ValueError("C opt must be 8 characters long")
        
        self.first_line = self.first_line[0:24] + new_c_opt + self.first_line[32:]

        self._c_opt = new_c_opt

    @property
    def epslin(self):
        return self._epslin
    
    @epslin.setter
    def epslin(self, new_epslin):
        if len(new_epslin) != 8:
            raise ValueError("Epslin must be 8 characters long")
        
        self.first_line = self.first_line[0:32] + new_epslin + self.first_line[40:]

        self._epslin = new_epslin
    
    @property
    def tolmat(self):
        return self._tolmat
    
    @tolmat.setter
    def tolmat(self, new_tolmat):
        if len(new_tolmat) != 8:
            raise ValueError("Tolmat must be 8 characters long")
        
        self.first_line = self.first_line[0:40] + new_tolmat + self.first_line[48:]

        self._tolmat = new_tolmat
    
    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 8:
            raise ValueError("Tstart must be 8 characters long")
        
        self.first_line = self.first_line[0:48] + new_tstart

        self._tstart = new_tstart

    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) != 8:
            raise ValueError("Iout must be 8 characters long")
        
        self.second_line = new_iout + self.second_line[8:]
        
        self._iout = new_iout

    @property
    def iplot(self):
        return self._iplot
    
    @iplot.setter
    def iplot(self, new_iplot):
        if len(new_iplot) != 8:
            raise ValueError("Iplot must be 8 characters long")
        
        self.second_line = self.second_line[0:8] + new_iplot + self.second_line[16:]

        self._iplot = new_iplot

    @property
    def idoubl(self):
        return self._idoubl
    
    @idoubl.setter
    def idoubl(self, new_idoubl):
        if len(new_idoubl) != 8:
            raise ValueError("Idoubl must be 8 characters long")
        
        self.second_line = self.second_line[0:16] + new_idoubl + self.second_line[24:]

        self._idoubl = new_idoubl

    @property
    def kout(self):
        return self._kout
    
    @kout.setter
    def kout(self, new_kout):
        if len(new_kout) != 8:
            raise ValueError("Kout must be 8 characters long")
        
        self.second_line = self.second_line[0:24] + new_kout + self.second_line[32:]

        self._kout = new_kout

    @property
    def maxout(self):
        return self._maxout
    
    @maxout.setter
    def maxout(self, new_maxout):
        if len(new_maxout) != 8:
            raise ValueError("Maxout must be 8 characters long")
        
        self.second_line = self.second_line[0:32] + new_maxout + self.second_line[40:]


        self._maxout = new_maxout
    
    @property
    def ipun(self):
        return self._ipun
    
    @ipun.setter
    def ipun(self, new_ipun):
        if len(new_ipun) != 8:
            raise ValueError("Ipun must be 8 characters long")
        
        self.second_line = self.second_line[0:40] + new_ipun + self.second_line[48:]

        self._ipun = new_ipun

    @property
    def memsav(self):
        return self._memsav
    
    @memsav.setter
    def memsav(self, new_memsav):
        if len(new_memsav) != 8:
            raise ValueError("Memsav must be 8 characters long")
        
        self.second_line = self.second_line[0:48] + new_memsav + self.second_line[56:]

        self._memsav = new_memsav

    @property
    def icat(self):
        return self._icat
    
    @icat.setter
    def icat(self, new_icat):
        if len(new_icat) != 8:
            raise ValueError("Icat must be 8 characters long")
        
        self.second_line = self.second_line[0:56] + new_icat + self.second_line[64:]

        self._icat = new_icat

    @property
    def nenerg(self):
        return self._nenerg
    
    @nenerg.setter
    def nenerg(self, new_nenerg):
        if len(new_nenerg) != 8:
            raise ValueError("Nenerg must be 8 characters long")
        
        self.second_line = self.second_line[0:64] + new_nenerg + self.second_line[72:]

        self._nenerg = new_nenerg

    @property
    def iprsup(self):
        return self._iprsup
    
    @iprsup.setter
    def iprsup(self, new_iprsup):
        if len(new_iprsup) != 8:
            raise ValueError("Iprsup must be 8 characters long")
        
        self.second_line = self.second_line[0:72] + new_iprsup

        self._iprsup = new_iprsup

    

    
    
    @property
    def first_line(self):
        return self._first_line
    
    @first_line.setter
    def first_line(self, new_first_line):
        if len(new_first_line) != 56:
            raise ValueError("First line must be 56 characters long")
        
        self._delta_t = new_first_line[0:8]
        self._t_max = new_first_line[8:16]
        self._x_opt = new_first_line[16:24]
        self._c_opt = new_first_line[24:32]
        self._epslin = new_first_line[32:40]
        self._tolmat = new_first_line[40:48]
        self._tstart = new_first_line[48:56]

        self._first_line = new_first_line


    @property
    def second_line(self):
        return self._second_line
    
    @second_line.setter
    def second_line(self, new_second_line):
        if len(new_second_line) != 80:
            raise ValueError("Second line must be 80 characters long")
        
        self._iout = new_second_line[0:8]
        self._iplot = new_second_line[8:16]
        self._idoubl = new_second_line[16:24]
        self._kout = new_second_line[24:32]
        self._maxout = new_second_line[32:40]
        self._ipun = new_second_line[40:48]
        self._memsav = new_second_line[48:56]
        self._icat = new_second_line[56:64]
        self._nenerg = new_second_line[64:72]
        self._iprsup = new_second_line[72:80]

        self._second_line = new_second_line

    def write(self): 
        return f"{self.comment_line}\n{self.first_line}\n{self.second_line}\n"

class Models:
    def __init__(self) -> None:
        pass

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
        if len(new_itype) != 2:
            raise ValueError("Itype must be 2 characters long")
        
        self._line = new_itype + self._line[2:]
        self._itype = new_itype

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) != 6:
            raise ValueError("Node 1 must be 6 characters long")
        
        self._line = self._line[0:2] + new_node_1 + self._line[8:]

        self._node_1 = new_node_1
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) != 6:
            raise ValueError("Node 2 must be 6 characters long")
        
        self._line = self._line[0:8] + new_node_2 + self._line[14:]

        self._node_2 = new_node_2
    
    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter
    def node_ref_1(self, new_node_ref_1):
        if len(new_node_ref_1) != 6:
            raise ValueError("Node ref 1 must be 6 characters long")
        
        self._line = self._line[0:14] + new_node_ref_1 + self._line[20:]

        self._node_ref_1 = new_node_ref_1

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter
    def node_ref_2(self, new_node_ref_2):
        if len(new_node_ref_2) != 6:
            raise ValueError("Node ref 2 must be 6 characters long")
        
        self._line = self._line[0:20] + new_node_ref_2 + self._line[26:]

        self._node_ref_2 = new_node_ref_2
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, new_resistance):
        if len(new_resistance) != 6:
            raise ValueError("Resistance must be 6 characters long")
        
        self._line = self._line[0:26] + new_resistance + self._line[32:]

        self._resistance = new_resistance
    
    @property
    def inductance(self):
        return self._inductance
    
    @inductance.setter
    def inductance(self, new_inductance):
        if len(new_inductance) != 6:
            raise ValueError("Inductance must be 6 characters long")
        
        self._line = self._line[0:32] + new_inductance + self._line[38:]

        self._inductance = new_inductance
    
    @property
    def capacitance(self):
        return self._capacitance
    
    @capacitance.setter
    def capacitance(self, new_capacitance):
        if len(new_capacitance) != 6:
            raise ValueError("Capacitance must be 6 characters long")
        
        self._line = self._line[0:38] + new_capacitance + self._line[44:]
        
        self._capacitance = new_capacitance
    
    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) != 1:
            raise ValueError("Iout must be 1 characters long")
        
        self._line = self._line[0:79] + new_iout

        self._iout = new_iout

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) != 80:
            raise ValueError("Line must be 80 characters long")
        
        self._line = new_line

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
        if len(new_itype) != 2:
            raise ValueError("Itype must be 2 characters long")
        
        self._line = new_itype + self._line[2:]

        self._itype = new_itype

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) != 6:
            raise ValueError("Node 1 must be 6 characters long")
        
        self._line = self._line[0:2] + new_node_1 + self._line[8:]

        self._node_1 = new_node_1
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) != 6:
            raise ValueError("Node 2 must be 6 characters long")
        
        self._line = self._line[0:8] + new_node_2 + self._line[14:]

        self._node_2 = new_node_2

    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter
    def node_ref_1(self, new_node_ref_1):
        if len(new_node_ref_1) != 6:
            raise ValueError("Node ref 1 must be 6 characters long")
        
        self._line = self._line[0:14] + new_node_ref_1 + self._line[20:]

        self._node_ref_1 = new_node_ref_1

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter
    def node_ref_2(self, new_node_ref_2):
        if len(new_node_ref_2) != 6:
            raise ValueError("Node ref 2 must be 6 characters long")
        
        self._line = self._line[0:20] + new_node_ref_2 + self._line[26:]

        self._node_ref_2 = new_node_ref_2
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, new_resistance):
        if len(new_resistance) != 6:
            raise ValueError("Resistance must be 6 characters long")
        
        self._line = self._line[0:26] + new_resistance + self._line[32:]

        self._resistance = new_resistance
    
    @property
    def distribution_param_a(self):
        return self._distribution_param_a
    
    @distribution_param_a.setter
    def distribution_param_a(self, new_distribution_param_a):
        if len(new_distribution_param_a) != 6:
            raise ValueError("Distribution param a must be 6 characters long")
        
        self._line = self._line[0:32] + new_distribution_param_a + self._line[38:]
        self._distribution_param_a = new_distribution_param_a
    
    @property
    def distribution_param_b(self):
        return self._distribution_param_b
    
    @distribution_param_b.setter
    def distribution_param_b(self, new_distribution_param_b):
        if len(new_distribution_param_b) != 6:
            raise ValueError("Distribution param b must be 6 characters long")
        
        self._line = self._line[0:38] + new_distribution_param_b + self._line[44:]

        self._distribution_param_b = new_distribution_param_b
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_length):
        if len(new_length) != 6:
            raise ValueError("Length must be 6 characters long")
        
        self._line = self._line[0:44] + new_length + self._line[50:]

        self._length = new_length

    @property
    def iline(self):
        return self._iline

    @iline.setter
    def iline(self, new_iline):
        if len(new_iline) != 2:
            raise ValueError("Iline must be 2 characters long")
        
        self._line = self._line[0:50] + new_iline + self._line[52:]
        self._iline = new_iline

    @property
    def ipunch(self):
        return self._ipunch
    
    @ipunch.setter
    def ipunch(self, new_ipunch):
        if len(new_ipunch) != 2:
            raise ValueError("Ipunch must be 2 characters long")
        
        self._line = self._line[0:52] + new_ipunch + self._line[54:]
        self._ipunch = new_ipunch
    
    @property
    def ipose(self):
        return self._ipose
    
    @ipose.setter
    def ipose(self, new_ipose):
        if len(new_ipose) != 2:
            raise ValueError("Ipose must be 2 characters long")
        
        self._line = self._line[0:54] + new_ipose + self._line[56:]
        self._ipose = new_ipose
    
    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) != 1:
            raise ValueError("Iout must be 1 characters long")
        
        self._line = self._line[0:79] + new_iout
        self._iout = new_iout
    


class Switch:
    def __init__(self) -> None:
        self.init_line = "/SWITCH\n"
        self.comment_line = "C < n 1>< n 2>< Tclose ><Top/Tde ><   Ie   ><Vf/CLOP ><  type  >\n"
    	
        self.switches = []

    def write(self):
        return self.init_line + self.comment_line + "".join([switch.write() for switch in self.switches])

    def add_switch(self, switch):
        if not isinstance(switch, SwitchElement):
            raise TypeError("Switch must be of type SwitchElement")
        self.switches.append(switch)


class SwitchElement:
    def __init__(self) -> None:

        line_str_len = 80
        self._line = " " * line_str_len
        
        itype_str_len = 2
        self._itype = " " * itype_str_len

        node_str_len = 6
        self._node_1 = " " * node_str_len
        self._node_2 = " " * node_str_len

        t_close_delay_str_len = 10

        self._t_close = " " * t_close_delay_str_len
        self._t_delay = " " * t_close_delay_str_len

        current_str_len = 10

        self._current = " " * current_str_len

        vflash_clop_str_len = 10

        self._vflash_clop = " " * vflash_clop_str_len

        type_str_len = 2

        self._type = " " * type_str_len

        self.blank_str_len = 14

        self._blank = " " * self.blank_str_len

        self._iout = " "

    def write(self):
        return f"{self.line}\n"

    @property
    def itype(self):
        return self._itype

    @itype.setter
    def itype(self, new_itype):
        if len(new_itype) != 2:
            raise ValueError("Itype must be 2 characters long")
        
        self._line = new_itype + self._line[2:]

        self._itype = new_itype

    @property
    def node_1(self):
        return self._node_1

    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) != 6:
            raise ValueError("Node 1 must be 6 characters long")
        
        self._line = self._line[0:2] + new_node_1 + self._line[8:]

        self._node_1 = new_node_1

    @property
    def node_2(self):
        return self._node_2

    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) != 6:
            raise ValueError("Node 2 must be 6 characters long")
        
        self._line = self._line[0:8] + new_node_2 + self._line[14:]

        self._node_2 = new_node_2

    @property
    def t_close(self):
        return self._t_close

    @t_close.setter
    def t_close(self, new_t_close):
        if len(new_t_close) != 10:
            raise ValueError("T close must be 10 characters long")
        
        self._line = self._line[0:14] + new_t_close + self._line[24:]

        self._t_close = new_t_close

    @property
    def t_delay(self):
        return self._t_delay
    
    @t_delay.setter
    def t_delay(self, new_t_delay):
        if len(new_t_delay) != 10:
            raise ValueError("T delay must be 10 characters long")
        
        self._line = self._line[0:24] + new_t_delay + self._line[34:]

        self._t_delay = new_t_delay

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, new_current):
        if len(new_current) != 10:
            raise ValueError("Current must be 10 characters long")
        
        self._line = self._line[0:34] + new_current + self._line[44:]

        self._current = new_current
    
    @property
    def vflash_clop(self):
        return self._vflash_clop
    
    @vflash_clop.setter
    def vflash_clop(self, new_vflash_clop):
        if len(new_vflash_clop) != 10:
            raise ValueError("Vflash clop must be 10 characters long")
        
        self._line = self._line[0:44] + new_vflash_clop + self._line[54:]

        self._vflash_clop = new_vflash_clop

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        if len(new_type) != 2:
            raise ValueError("Type must be 2 characters long")
        
        self._line = self._line[0:54] + new_type + self._line[56:]

        self._type = new_type

    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) != 1:
            raise ValueError("Iout must be 1 characters long")
        
        self._line = self._line[0:79] + new_iout

        self._iout = new_iout


class Source:
    def __init__(self) -> None:
        pass

class Output:
    def __init__(self) -> None:
        self._init_line = "/OUTPUT\n"
        line_str_len = 80
        self._line = " " * line_str_len
        
        blank_str_len = 2
        self._blank = " " * blank_str_len

        vars_str_len = 6
        self._vars = [" " * vars_str_len for i in range(13)]


    def write(self):
        return self._init_line + self._line + '\n' if self._line != " " * 80 else self._init_line 
        
    def set_vars(self, vars):
        # The user can put less than 13 vars
        # if he puts less, the rest will be filled with blanks

        if len(vars) > 13:
            raise ValueError("There can be at most 13 vars")
        
        # I have to make sure that the vars are 6 characters long, adding blanks if necessary

        for i in range(len(vars)):
            if len(vars[i]) != 6:
                vars[i] = vars[i] + " " * (6 - len(vars[i]))
        
        self.vars = vars

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, new_line):
        
        self._line = new_line

        self._blank = new_line[0:2]

        # split by vars_str_len
        self.vars = [new_line[i:i+6] for i in range(2, len(new_line), 6)]

        # add blanks if necessary
        self.vars = [var + " " * (6 - len(var)) for var in self.vars]

    @property
    def vars(self):
        return self._vars
    
    @vars.setter
    def vars(self, new_vars):
        
        self._line = self._blank + "".join(new_vars)

        self._vars = new_vars

    

class Plot:
    def __init__(self) -> None:
        pass

