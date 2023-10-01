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

    def write(self):
        pass 



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
        
        self.first_line[0:8] = new_delta_t

        self._delta_t = new_delta_t

    @property
    def t_max(self):
        return self._t_max
    
    @t_max.setter
    def t_max(self, new_t_max):
        if len(new_t_max) != 8:
            raise ValueError("T max must be 8 characters long")
        
        self.first_line[8:16] = new_t_max

        self._t_max = new_t_max

    @property
    def x_opt(self):
        return self._x_opt
    
    @x_opt.setter
    def x_opt(self, new_x_opt):
        if len(new_x_opt) != 8:
            raise ValueError("X opt must be 8 characters long")
        
        self.first_line[16:24] = new_x_opt

        self._x_opt = new_x_opt
    
    @property
    def c_opt(self):
        return self._c_opt
    
    @c_opt.setter
    def c_opt(self, new_c_opt):
        if len(new_c_opt) != 8:
            raise ValueError("C opt must be 8 characters long")
        
        self.first_line[24:32] = new_c_opt

        self._c_opt = new_c_opt

    @property
    def epslin(self):
        return self._epslin
    
    @epslin.setter
    def epslin(self, new_epslin):
        if len(new_epslin) != 8:
            raise ValueError("Epslin must be 8 characters long")
        
        self.first_line[32:40] = new_epslin

        self._epslin = new_epslin
    
    @property
    def tolmat(self):
        return self._tolmat
    
    @tolmat.setter
    def tolmat(self, new_tolmat):
        if len(new_tolmat) != 8:
            raise ValueError("Tolmat must be 8 characters long")
        
        self.first_line[40:48] = new_tolmat

        self._tolmat = new_tolmat
    
    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 8:
            raise ValueError("Tstart must be 8 characters long")
        
        self.first_line[48:56] = new_tstart

        self._tstart = new_tstart

    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) != 8:
            raise ValueError("Iout must be 8 characters long")
        
        self.second_line[0:8] = new_iout

        self._iout = new_iout

    @property
    def iplot(self):
        return self._iplot
    
    @iplot.setter
    def iplot(self, new_iplot):
        if len(new_iplot) != 8:
            raise ValueError("Iplot must be 8 characters long")
        
        self.second_line[8:16] = new_iplot

        self._iplot = new_iplot

    @property
    def idoubl(self):
        return self._idoubl
    
    @idoubl.setter
    def idoubl(self, new_idoubl):
        if len(new_idoubl) != 8:
            raise ValueError("Idoubl must be 8 characters long")
        
        self.second_line[16:24] = new_idoubl

        self._idoubl = new_idoubl

    @property
    def kout(self):
        return self._kout
    
    @kout.setter
    def kout(self, new_kout):
        if len(new_kout) != 8:
            raise ValueError("Kout must be 8 characters long")
        
        self.second_line[24:32] = new_kout

        self._kout = new_kout

    @property
    def maxout(self):
        return self._maxout
    
    @maxout.setter
    def maxout(self, new_maxout):
        if len(new_maxout) != 8:
            raise ValueError("Maxout must be 8 characters long")
        
        self.second_line[32:40] = new_maxout

        self._maxout = new_maxout
    
    @property
    def ipun(self):
        return self._ipun
    
    @ipun.setter
    def ipun(self, new_ipun):
        if len(new_ipun) != 8:
            raise ValueError("Ipun must be 8 characters long")
        
        self.second_line[40:48] = new_ipun

        self._ipun = new_ipun

    @property
    def memsav(self):
        return self._memsav
    
    @memsav.setter
    def memsav(self, new_memsav):
        if len(new_memsav) != 8:
            raise ValueError("Memsav must be 8 characters long")
        
        self.second_line[48:56] = new_memsav

        self._memsav = new_memsav

    @property
    def icat(self):
        return self._icat
    
    @icat.setter
    def icat(self, new_icat):
        if len(new_icat) != 8:
            raise ValueError("Icat must be 8 characters long")
        
        self.second_line[56:64] = new_icat

        self._icat = new_icat

    @property
    def nenerg(self):
        return self._nenerg
    
    @nenerg.setter
    def nenerg(self, new_nenerg):
        if len(new_nenerg) != 8:
            raise ValueError("Nenerg must be 8 characters long")
        
        self.second_line[64:72] = new_nenerg

        self._nenerg = new_nenerg

    @property
    def iprsup(self):
        return self._iprsup
    
    @iprsup.setter
    def iprsup(self, new_iprsup):
        if len(new_iprsup) != 8:
            raise ValueError("Iprsup must be 8 characters long")
        
        self.second_line[72:80] = new_iprsup

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
    def __init__(self) -> None:
        self.comment_line_type_0 = "C < n1 >< n2 ><ref1><ref2>< R  >< L  >< C  >"
        self.comment_line_distrib_params = "C < n1 >< n2 ><ref1><ref2>< R  >< A  >< B  ><Leng><><>0"

        self.branches = []

        pass


class RlcElement:
    def __init__(self) -> None:
        itype_str_len = 2
        self._itype = " " * itype_str_len

        node_str_len = 6
        self._node_1 = " " * node_str_len
        self._node_2 = " " * node_str_len
        self._node_ref_1  = " " * node_str_len
        self._node_ref_2  = " " * node_str_len

        resistance_str_len = 6

        self._resistance = " " * resistance_str_len

    def write(self):

        pass


class RlcElementBasic(RlcElement):
    def __init__(self) -> None:
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
        
        self._line[0:2] = new_itype

        self._itype = new_itype

    @property
    def node_1(self):
        return self._node_1
    
    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) != 6:
            raise ValueError("Node 1 must be 6 characters long")
        
        self._line[2:8] = new_node_1

        self._node_1 = new_node_1
    
    @property
    def node_2(self):
        return self._node_2
    
    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) != 6:
            raise ValueError("Node 2 must be 6 characters long")
        
        self._line[8:14] = new_node_2

        self._node_2 = new_node_2
    
    @property
    def node_ref_1(self):
        return self._node_ref_1
    
    @node_ref_1.setter
    def node_ref_1(self, new_node_ref_1):
        if len(new_node_ref_1) != 6:
            raise ValueError("Node ref 1 must be 6 characters long")
        
        self._line[14:20] = new_node_ref_1

        self._node_ref_1 = new_node_ref_1

    @property
    def node_ref_2(self):
        return self._node_ref_2
    
    @node_ref_2.setter
    def node_ref_2(self, new_node_ref_2):
        if len(new_node_ref_2) != 6:
            raise ValueError("Node ref 2 must be 6 characters long")
        
        self._line[20:26] = new_node_ref_2

        self._node_ref_2 = new_node_ref_2
    
    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, new_resistance):
        if len(new_resistance) != 6:
            raise ValueError("Resistance must be 6 characters long")
        
        self._line[26:32] = new_resistance

        self._resistance = new_resistance
    
    @property
    def inductance(self):
        return self._inductance
    
    @inductance.setter
    def inductance(self, new_inductance):
        if len(new_inductance) != 6:
            raise ValueError("Inductance must be 6 characters long")
        
        self._line[32:38] = new_inductance

        self._inductance = new_inductance
    
    @property
    def capacitance(self):
        return self._capacitance
    
    @capacitance.setter
    def capacitance(self, new_capacitance):
        if len(new_capacitance) != 6:
            raise ValueError("Capacitance must be 6 characters long")
        
        self._line[38:44] = new_capacitance

        self._capacitance = new_capacitance
    
    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) != 1:
            raise ValueError("Iout must be 1 characters long")
        
        self._line[79] = new_iout

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
    def __init__(self) -> None:
        super().__init__()

        line_len = 80
        self._line = " " * line_len

        type_len = 2
        self._distribution_type = " " * type_len

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

class Switch:
    def __init__(self) -> None:
        pass

class Source:
    def __init__(self) -> None:
        pass

class Output:
    def __init__(self) -> None:
        pass

class Plot:
    def __init__(self) -> None:
        pass

