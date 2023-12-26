import copy 
from utils import bool_to_valid_str, numeric_to_valid_str

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

        try:
            float(new_delta_t)
        except ValueError:
            raise ValueError("Delta t must be a number")
        
        new_delta_t = numeric_to_valid_str(new_delta_t, spot_len=8) 

        if len(new_delta_t) > 8:
            raise ValueError("Delta t cant be longer than 8 characters long")
        
        self.first_line = new_delta_t.ljust(8) + self.first_line[8:]
        

        self._delta_t = new_delta_t.ljust(8)

    @property
    def t_max(self):
        return self._t_max

    @t_max.setter
    def t_max(self, new_t_max):

        try:
            float(new_t_max)
        except ValueError:
            raise ValueError("T max must be a number")
        
        new_t_max = numeric_to_valid_str(new_t_max, spot_len=8)


        if len(new_t_max) > 8:
            raise ValueError("T max cant be longer than 8 characters long")

        self.first_line = self.first_line[0:8] + new_t_max.ljust(8) + self.first_line[16:]

        self._t_max = new_t_max.ljust(8)

    @property
    def x_opt(self):
        return self._x_opt

    @x_opt.setter
    def x_opt(self, new_x_opt):

        if type(new_x_opt) != str:
            new_x_opt = bool_to_valid_str(bool(new_x_opt))
            new_x_opt = new_x_opt.ljust(8)

        if len(new_x_opt) > 8:
            raise ValueError("X opt cant be longer than 8 characters long")

        self.first_line = self.first_line[0:16] + new_x_opt.ljust(8) + self.first_line[24:]

        self._x_opt = new_x_opt.ljust(8)

    @property
    def c_opt(self):
        return self._c_opt

    @c_opt.setter
    def c_opt(self, new_c_opt):

        if type(new_c_opt) != str:
            new_c_opt = bool_to_valid_str(bool(new_c_opt))
            new_c_opt = new_c_opt.ljust(8)

        if len(new_c_opt) > 8:
            raise ValueError("C opt cant be longer than 8 characters long")

        self.first_line = self.first_line[0:24] + new_c_opt.ljust(8) + self.first_line[32:]

        self._c_opt = new_c_opt.ljust(8)

    @property
    def epslin(self):
        return self._epslin

    @epslin.setter
    def epslin(self, new_epslin):

        if type(new_epslin) != str:
            new_epslin = bool_to_valid_str(bool(new_epslin))
            new_epslin = new_epslin.ljust(8)


        if len(new_epslin) > 8:
            raise ValueError("Epslin cant be longer than 8 characters long")

        self.first_line = self.first_line[0:32] + new_epslin.ljust(8) + self.first_line[40:]

        self._epslin = new_epslin.ljust(8)

    @property
    def tolmat(self):
        return self._tolmat

    @tolmat.setter
    def tolmat(self, new_tolmat):

        if type(new_tolmat) != str:
            new_tolmat = bool_to_valid_str(bool(new_tolmat))
            new_tolmat = new_tolmat.ljust(8)


        if len(new_tolmat) > 8:
            raise ValueError("Tolmat cant be longer than 8 characters long")

        self.first_line = self.first_line[0:40] + new_tolmat.ljust(8) + self.first_line[48:]

        self._tolmat = new_tolmat.ljust(8)

    @property
    def tstart(self):
        return self._tstart

    @tstart.setter
    def tstart(self, new_tstart):


        if (new_tstart != " " * 8):
            try:
                float(new_tstart)
            except ValueError:
                raise ValueError("T start must be a number")
            
        new_tstart = numeric_to_valid_str(new_tstart, spot_len=8)

        if len(new_tstart) > 8:
            raise ValueError("Tstart cant be longer than 8 characters long")

        self.first_line = self.first_line[0:48] + new_tstart.ljust(8)

        self._tstart = new_tstart.ljust(8)

    @property
    def iout(self):
        return self._iout

    @iout.setter
    def iout(self, new_iout):

        try:
            int(new_iout)
        except ValueError:
            raise ValueError("Iout must be a number")
        
        new_iout = numeric_to_valid_str(new_iout, spot_len=8)

        if len(new_iout) > 8:
            raise ValueError("Iout cant be longer than 8 characters long")

        self.second_line = new_iout.ljust(8) + self.second_line[8:]

        self._iout = new_iout.ljust(8)

    @property
    def iplot(self):
        return self._iplot

    @iplot.setter
    def iplot(self, new_iplot):

        try:
            int(new_iplot)
        except ValueError:
            raise ValueError("Iplot must be a number")
        
        new_iplot = numeric_to_valid_str(new_iplot, spot_len=8)

        if len(new_iplot) > 8:
            raise ValueError("Iplot cant be longer than 8 characters long")

        self.second_line = self.second_line[0:8] + new_iplot.ljust(8) + self.second_line[16:]

        self._iplot = new_iplot.ljust(8)

    @property
    def idoubl(self):
        return self._idoubl

    @idoubl.setter
    def idoubl(self, new_idoubl):

        if type(new_idoubl) != str:
            new_idoubl = bool_to_valid_str(bool(new_idoubl))
            new_idoubl = new_idoubl.ljust(8)


        if len(new_idoubl) > 8:
            raise ValueError("Idoubl cant be longer than 8 characters long")

        self.second_line = self.second_line[0:16] + new_idoubl.ljust(8) + self.second_line[24:]

        self._idoubl = new_idoubl.ljust(8)

    @property
    def kout(self):
        return self._kout

    @kout.setter
    def kout(self, new_kout):

        if type(new_kout) != str:
            new_kout = bool_to_valid_str(bool(new_kout))
            new_kout = new_kout.ljust(8)
        

        if len(new_kout) > 8:
            raise ValueError("Kout cant be longer than 8 characters long")

        self.second_line = self.second_line[0:24] + new_kout.ljust(8) + self.second_line[32:]

        self._kout = new_kout.ljust(8)

    @property
    def maxout(self):
        return self._maxout

    @maxout.setter
    def maxout(self, new_maxout):

        if type(new_maxout) != str:
            new_maxout = bool_to_valid_str(bool(new_maxout))
            new_maxout = new_maxout.ljust(8)
        

        if len(new_maxout) > 8:
            raise ValueError("Maxout cant be longer than 8 characters long")

        self.second_line = self.second_line[0:32] + new_maxout.ljust(8) + self.second_line[40:]

        self._maxout = new_maxout.ljust(8)

    @property
    def ipun(self):
        return self._ipun

    @ipun.setter
    def ipun(self, new_ipun):

        if type(new_ipun) != str:
            new_ipun = bool_to_valid_str(bool(new_ipun))
            new_ipun = new_ipun.ljust(8)

        if len(new_ipun) > 8:
            raise ValueError("Ipun cant be longer than 8 characters long")

        self.second_line = self.second_line[0:40] + new_ipun.ljust(8) + self.second_line[48:]

        self._ipun = new_ipun.ljust(8)

    @property
    def memsav(self):
        return self._memsav

    @memsav.setter
    def memsav(self, new_memsav):

        if type(new_memsav) != str:
            new_memsav = bool_to_valid_str(bool(new_memsav))
            new_memsav = new_memsav.ljust(8)

        if len(new_memsav) > 8:
            raise ValueError("Memsav cant be longer than 8 characters long")

        self.second_line = self.second_line[0:48] + new_memsav.ljust(8) + self.second_line[56:]

        self._memsav = new_memsav.ljust(8)

    @property
    def icat(self):
        return self._icat

    @icat.setter
    def icat(self, new_icat):

        if type(new_icat) != str:
            new_icat = bool_to_valid_str(bool(new_icat))
            new_icat = new_icat.ljust(8)

        if len(new_icat) > 8:
            raise ValueError("Icat cant be longer than 8 characters long")

        self.second_line = self.second_line[0:56] + new_icat.ljust(8) + self.second_line[64:]

        self._icat = new_icat.ljust(8)

    @property
    def nenerg(self):
        return self._nenerg

    @nenerg.setter
    def nenerg(self, new_nenerg):

        if type(new_nenerg) != str:
            new_nenerg = bool_to_valid_str(bool(new_nenerg))
            new_nenerg = new_nenerg.ljust(8)

        if len(new_nenerg) > 8:
            raise ValueError("Nenerg cant be longer than 8 characters long")

        self.second_line = self.second_line[0:64] + new_nenerg.ljust(8) + self.second_line[72:]

        self._nenerg = new_nenerg.ljust(8)

    @property
    def iprsup(self):
        return self._iprsup

    @iprsup.setter
    def iprsup(self, new_iprsup):

        if type(new_iprsup) != str:
            new_iprsup = bool_to_valid_str(bool(new_iprsup))
            new_iprsup = new_iprsup.ljust(8)

        if len(new_iprsup) > 8:
            raise ValueError("Iprsup cant be longer than 8 characters long")

        self.second_line = self.second_line[0:72] + new_iprsup.ljust(8)

        self._iprsup = new_iprsup.ljust(8)
    
    @property
    def first_line(self):
        return self._first_line
    
    @first_line.setter
    def first_line(self, new_first_line):
        if len(new_first_line) > 56:
            raise ValueError("First line cant be longer than 56 characters long")
        
        #Adding blanks if necessary
        new_first_line = new_first_line.ljust(56)
        
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
        if len(new_second_line) > 80:
            raise ValueError("Second line cant be longer than 80 characters long")

        #Adding blanks if necessary
        new_second_line = new_second_line.ljust(80)
        
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
    
    def copy(self):
        return copy.deepcopy(self)

    def from_file(self, file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()

        # The lines start after the comment "C  dT  >< Tmax >< Xopt >< Copt ><Epsiln>""
        # And ends before the '/' character

        # Get the index of the first line
        first_line_index = -1
        last_line_index = -1

        for index, line in enumerate(lines):
            if line.startswith("C  dT  >< Tmax >< Xopt >< Copt ><Epsiln>"):
                first_line_index = index + 1
                break
        
        # Get the index of the last line
        for index, line in enumerate(lines):
            if line.startswith("/"):
                last_line_index = index
                break

        # Remove every line that its first character is a 'C'
        lines = [line for line in lines[first_line_index:last_line_index] if not line.startswith("C")]
        # Remove the '\n' character from the end of each line
        lines = [line[:-1] for line in lines]


        self.first_line = lines[0]
        self.second_line = lines[1]

        return self

