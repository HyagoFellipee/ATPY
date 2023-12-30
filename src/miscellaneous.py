import copy 
from utils import bool_to_valid_str, numeric_to_valid_str, cant_be_longer_message

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

        spot_len = 8

        try:
            float(new_delta_t)
        except ValueError:
            raise ValueError("Delta t must be a number")
        
        new_delta_t = numeric_to_valid_str(new_delta_t, spot_len) 

        if len(new_delta_t) > spot_len:
            raise ValueError(cant_be_longer_message("new_delta_t", spot_len))
        
        self.first_line = new_delta_t.rjust(spot_len) + self.first_line[spot_len:]
        

        self._delta_t = new_delta_t.rjust(spot_len)

    @property
    def t_max(self):
        return self._t_max

    @t_max.setter
    def t_max(self, new_t_max):

        spot_len = 8

        try:
            float(new_t_max)
        except ValueError:
            raise ValueError("T max must be a number")
        
        new_t_max = numeric_to_valid_str(new_t_max, spot_len)


        if len(new_t_max) > spot_len:
            raise ValueError(cant_be_longer_message("new_t_max", spot_len))

        self.first_line = self.first_line[0:spot_len] + new_t_max.rjust(spot_len) + self.first_line[spot_len*2:]

        self._t_max = new_t_max.rjust(spot_len)

    @property
    def x_opt(self):
        return self._x_opt

    @x_opt.setter
    def x_opt(self, new_x_opt):

        spot_len = 8

        if type(new_x_opt) != str:
            new_x_opt = bool_to_valid_str(bool(new_x_opt))
            new_x_opt = new_x_opt.rjust(spot_len)

        if len(new_x_opt) > spot_len:
            raise ValueError(cant_be_longer_message("new_x_opt", spot_len))

        self.first_line = self.first_line[0:spot_len*2] + new_x_opt.rjust(spot_len) + self.first_line[spot_len*3:]

        self._x_opt = new_x_opt.rjust(spot_len)

    @property
    def c_opt(self):
        return self._c_opt

    @c_opt.setter
    def c_opt(self, new_c_opt):

        spot_len = 8

        if type(new_c_opt) != str:
            new_c_opt = bool_to_valid_str(bool(new_c_opt))
            new_c_opt = new_c_opt.rjust(spot_len)

        if len(new_c_opt) > spot_len:
            raise ValueError(cant_be_longer_message("new_c_opt", spot_len))

        self.first_line = self.first_line[0:spot_len*3] + new_c_opt.rjust(spot_len) + self.first_line[spot_len*4:]

        self._c_opt = new_c_opt.rjust(spot_len)

    @property
    def epslin(self):
        return self._epslin

    @epslin.setter
    def epslin(self, new_epslin):

        spot_len = 8

        if type(new_epslin) != str:
            new_epslin = bool_to_valid_str(bool(new_epslin))
            new_epslin = new_epslin.rjust(spot_len)


        if len(new_epslin) > spot_len:
            raise ValueError(cant_be_longer_message("new_epslin", spot_len))

        self.first_line = self.first_line[0:spot_len*4] + new_epslin.rjust(spot_len) + self.first_line[spot_len*5:]

        self._epslin = new_epslin.rjust(spot_len)

    @property
    def tolmat(self):
        return self._tolmat

    @tolmat.setter
    def tolmat(self, new_tolmat):

        spot_len = 8

        if type(new_tolmat) != str:
            new_tolmat = bool_to_valid_str(bool(new_tolmat))
            new_tolmat = new_tolmat.rjust(spot_len)


        if len(new_tolmat) > spot_len:
            raise ValueError(cant_be_longer_message("new_tolmat", spot_len))

        self.first_line = self.first_line[0:spot_len*5] + new_tolmat.rjust(spot_len) + self.first_line[spot_len*6:]

        self._tolmat = new_tolmat.rjust(spot_len)

    @property
    def tstart(self):
        return self._tstart

    @tstart.setter
    def tstart(self, new_tstart):

        spot_len = 8


        if (new_tstart != " " * 8):
            try:
                float(new_tstart)
            except ValueError:
                raise ValueError("T start must be a number")
            
        new_tstart = numeric_to_valid_str(new_tstart, spot_len)

        if len(new_tstart) > spot_len:
            raise ValueError(cant_be_longer_message("new_tstart", spot_len))

        self.first_line = self.first_line[0:spot_len*6] + new_tstart.rjust(spot_len)

        self._tstart = new_tstart.rjust(spot_len)

    @property
    def iout(self):
        return self._iout

    @iout.setter
    def iout(self, new_iout):

        spot_len = 8

        new_iout = numeric_to_valid_str(new_iout, spot_len)

        if len(new_iout) > spot_len:
            raise ValueError(cant_be_longer_message("new_iout", spot_len))

        self.second_line = new_iout.rjust(spot_len) + self.second_line[spot_len:]

        self._iout = new_iout.rjust(spot_len)

    @property
    def iplot(self):
        return self._iplot

    @iplot.setter
    def iplot(self, new_iplot):

        spot_len = 8

        try:
            int(new_iplot)
        except ValueError:
            raise ValueError("Iplot must be a number")
        
        new_iplot = numeric_to_valid_str(new_iplot, spot_len)

        if len(new_iplot) > spot_len:
            raise ValueError(cant_be_longer_message("new_iplot", spot_len))

        self.second_line = self.second_line[0:spot_len] + new_iplot.rjust(spot_len) + self.second_line[spot_len*2:]

        self._iplot = new_iplot.rjust(spot_len)

    @property
    def idoubl(self):
        return self._idoubl

    @idoubl.setter
    def idoubl(self, new_idoubl):

        spot_len = 8

        if type(new_idoubl) != str:
            new_idoubl = bool_to_valid_str(bool(new_idoubl))
            new_idoubl = new_idoubl.rjust(spot_len)


        if len(new_idoubl) > spot_len:
            raise ValueError(cant_be_longer_message("new_idoubl", spot_len))

        self.second_line = self.second_line[0:spot_len*2] + new_idoubl.rjust(spot_len) + self.second_line[spot_len*3:]

        self._idoubl = new_idoubl.rjust(spot_len)

    @property
    def kout(self):
        return self._kout

    @kout.setter
    def kout(self, new_kout):

        spot_len = 8

        if type(new_kout) != str:
            new_kout = bool_to_valid_str(bool(new_kout))
            new_kout = new_kout.rjust(spot_len)
        

        if len(new_kout) > spot_len:
            raise ValueError(cant_be_longer_message("new_kout", spot_len))

        self.second_line = self.second_line[0:spot_len*3] + new_kout.rjust(spot_len) + self.second_line[spot_len*4:]

        self._kout = new_kout.rjust(spot_len)

    @property
    def maxout(self):
        return self._maxout

    @maxout.setter
    def maxout(self, new_maxout):

        spot_len = 8

        if type(new_maxout) != str:
            new_maxout = bool_to_valid_str(bool(new_maxout))
            new_maxout = new_maxout.rjust(spot_len)
        

        if len(new_maxout) > spot_len:
            raise ValueError(cant_be_longer_message("new_maxout", spot_len))

        self.second_line = self.second_line[0:spot_len*4] + new_maxout.rjust(spot_len) + self.second_line[spot_len*5:]

        self._maxout = new_maxout.rjust(spot_len)

    @property
    def ipun(self):
        return self._ipun

    @ipun.setter
    def ipun(self, new_ipun):

        spot_len = 8

        if type(new_ipun) != str:
            new_ipun = bool_to_valid_str(bool(new_ipun))
            new_ipun = new_ipun.rjust(spot_len)

        if len(new_ipun) > spot_len:
            raise ValueError(cant_be_longer_message("new_ipun", spot_len))

        self.second_line = self.second_line[0:spot_len*5] + new_ipun.rjust(spot_len) + self.second_line[spot_len*6:]

        self._ipun = new_ipun.rjust(spot_len)

    @property
    def memsav(self):
        return self._memsav

    @memsav.setter
    def memsav(self, new_memsav):

        spot_len = 8

        if type(new_memsav) != str:
            new_memsav = bool_to_valid_str(bool(new_memsav))
            new_memsav = new_memsav.rjust(spot_len)

        if len(new_memsav) > spot_len:
            raise ValueError(cant_be_longer_message("new_memsav", spot_len))

        self.second_line = self.second_line[0:spot_len*6] + new_memsav.rjust(spot_len) + self.second_line[spot_len*7:]

        self._memsav = new_memsav.rjust(spot_len)

    @property
    def icat(self):
        return self._icat

    @icat.setter
    def icat(self, new_icat):

        spot_len = 8

        if type(new_icat) != str:
            new_icat = bool_to_valid_str(bool(new_icat))
            new_icat = new_icat.rjust(spot_len)

        if len(new_icat) > spot_len:
            raise ValueError(cant_be_longer_message("new_icat", spot_len))

        self.second_line = self.second_line[0:spot_len*7] + new_icat.rjust(spot_len) + self.second_line[spot_len*8:]

        self._icat = new_icat.rjust(spot_len)

    @property
    def nenerg(self):
        return self._nenerg

    @nenerg.setter
    def nenerg(self, new_nenerg):

        spot_len = 8

        if type(new_nenerg) != str:
            new_nenerg = bool_to_valid_str(bool(new_nenerg))
            new_nenerg = new_nenerg.rjust(spot_len)

        if len(new_nenerg) > spot_len:
            raise ValueError(cant_be_longer_message("new_nenerg", spot_len))

        self.second_line = self.second_line[0:spot_len*8] + new_nenerg.rjust(spot_len) + self.second_line[spot_len*9:]

        self._nenerg = new_nenerg.rjust(spot_len)

    @property
    def iprsup(self):
        return self._iprsup

    @iprsup.setter
    def iprsup(self, new_iprsup):

        spot_len = 8

        if type(new_iprsup) != str:
            new_iprsup = bool_to_valid_str(bool(new_iprsup))
            new_iprsup = new_iprsup.rjust(spot_len)

        if len(new_iprsup) > spot_len:
            raise ValueError(cant_be_longer_message("new_iprsup", spot_len))

        self.second_line = self.second_line[0:spot_len*9] + new_iprsup.rjust(spot_len)

        self._iprsup = new_iprsup.rjust(spot_len)
    
    @property
    def first_line(self):
        return self._first_line
    
    @first_line.setter
    def first_line(self, new_first_line):

        spot_len = 8

        line_len = 56

        if len(new_first_line) > line_len:
            raise ValueError(cant_be_longer_message('new_first_line', line_len))
        
        #Adding blanks if necessary
        new_first_line = new_first_line.ljust(line_len)
        
        self._delta_t = new_first_line[0:spot_len]
        self._t_max = new_first_line[spot_len:spot_len*2]
        self._x_opt = new_first_line[spot_len*2:spot_len*3]
        self._c_opt = new_first_line[spot_len*3:spot_len*4]
        self._epslin = new_first_line[spot_len*4:spot_len*5]
        self._tolmat = new_first_line[spot_len*5:spot_len*6]
        self._tstart = new_first_line[spot_len*6:spot_len*7]

        self._first_line = new_first_line


    @property
    def second_line(self):
        return self._second_line
    
    @second_line.setter
    def second_line(self, new_second_line):

        spot_len = 8

        line_len = 80

        if len(new_second_line) > line_len:
            raise ValueError(cant_be_longer_message('new_second_line', line_len))

        #Adding blanks if necessary
        new_second_line = new_second_line.ljust(line_len)
        
        self._iout = new_second_line[0:spot_len]
        self._iplot = new_second_line[spot_len:spot_len*2]
        self._idoubl = new_second_line[spot_len*2:spot_len*3]
        self._kout = new_second_line[spot_len*3:spot_len*4]
        self._maxout = new_second_line[spot_len*4:spot_len*5]
        self._ipun = new_second_line[spot_len*5:spot_len*6]
        self._memsav = new_second_line[spot_len*6:spot_len*7]
        self._icat = new_second_line[spot_len*7:spot_len*8]
        self._nenerg = new_second_line[spot_len*8:spot_len*9]
        self._iprsup = new_second_line[spot_len*9:spot_len*10]

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

