import copy 

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

    def copy(self):
        return copy.deepcopy(self)
    

    def from_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        first_line_index = -1
        last_line_index = -1

        for index, line in enumerate(lines):
            if line.startswith("/SWITCH"):
                first_line_index = index + 1
                break

        for index, line in enumerate(lines[first_line_index:]):
            if line.startswith("/"):
                last_line_index = index + first_line_index
                break

        lines = [line for line in lines[first_line_index:last_line_index] if not line.startswith("C")]
        lines = [line[:-1] for line in lines]

        for line in lines:
            switch = SwitchElement()
            switch.line = line
            self.add_switch(switch)

        return self

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

    def copy(self):
        return copy.deepcopy(self)
    
    def write(self):
        return f"{self.line}\n"

    @property
    def itype(self):
        return self._itype

    @itype.setter
    def itype(self, new_itype):
        if len(new_itype) > 2:
            raise ValueError("Itype can't be longer than 2 characters")
        
        self._line = new_itype.ljust(2) + self._line[2:]

        self._itype = new_itype.ljust(2)

    @property
    def node_1(self):
        return self._node_1

    @node_1.setter
    def node_1(self, new_node_1):
        if len(new_node_1) > 6:
            raise ValueError("Node 1 can't be longer than 6 characters long")
        
        self._line = new_node_1.ljust(6) + self._line[6:]

        self._node_1 = new_node_1.ljust(6)

    @property
    def node_2(self):
        return self._node_2

    @node_2.setter
    def node_2(self, new_node_2):
        if len(new_node_2) > 6:
            raise ValueError("Node 2 can't be longer than 6 characters long")
        
        self._line = self._line[0:8] + new_node_2.ljust(6) + self._line[14:]

        self._node_2 = new_node_2.ljust(6)

    @property
    def t_close(self):
        return self._t_close

    @t_close.setter
    def t_close(self, new_t_close):
        if len(new_t_close) > 10:
            raise ValueError("T close can't be longer than 10 characters long")
        
        self._line = self._line[0:14] + new_t_close.ljust(10) + self._line[24:]

        self._t_close = new_t_close.ljust(10)

    @property
    def t_delay(self):
        return self._t_delay
    
    @t_delay.setter
    def t_delay(self, new_t_delay):
        if len(new_t_delay) > 10:
            raise ValueError("T delay can't be longer than 10 characters long")
        
        self._line = self._line[0:24] + new_t_delay.ljust(10) + self._line[34:]

        self._t_delay = new_t_delay.ljust(10)

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, new_current):
        if len(new_current) > 10:
            raise ValueError("Current can't be longer than 10 characters long")
        
        self._line = self._line[0:34] + new_current.ljust(10) + self._line[44:]

        self._current = new_current.ljust(10)
    
    @property
    def vflash_clop(self):
        return self._vflash_clop
    
    @vflash_clop.setter
    def vflash_clop(self, new_vflash_clop):
        if len(new_vflash_clop) > 10:
            raise ValueError("Vflash clop can't be longer than 10 characters long")
        
        self._line = self._line[0:44] + new_vflash_clop.ljust(10) + self._line[54:]

        self._vflash_clop = new_vflash_clop.ljust(10)

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        if len(new_type) > 2:
            raise ValueError("Type can't be longer than 2 characters long")
        
        self._line = self._line[0:54] + new_type.ljust(10) + self._line[56:]

        self._type = new_type.ljust(10)

    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) > 1:
            raise ValueError("Iout can't be longer than 1 characters long")
        
        self._line = self._line[0:79] + new_iout

        self._iout = new_iout

