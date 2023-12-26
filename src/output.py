import copy 

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

    def copy(self):
        return copy.deepcopy(self)

    def add_vars(self, vars):
        # The user can put less than 13 vars
        # if he puts less, the rest will be filled with blanks

        if len(vars) > 13:
            raise ValueError("There can be at most 13 vars")

        # I have to make sure that the vars are 6 characters long, adding blanks if necessary

        for i in range(len(vars)):
            if len(vars[i]) > 6:
                raise ValueError("Vars can't be longer than 6 characters")
            vars[i] = vars[i].ljust(6)

        self._line = self._blank + "".join(vars)     

        self._vars = vars

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
        self.vars = [var.ljust(6) for var in self.vars]

    @property
    def vars(self):
        return self._vars

    @vars.setter
    def vars(self, new_vars):

        self._vars = self.add_vars(new_vars)

    def from_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        first_line_index = -1
        last_line_index = -1

        for index, line in enumerate(lines):
            if line.startswith("/OUTPUT"):
                first_line_index = index + 1
                break

        for index, line in enumerate(lines[first_line_index:]):
            if line.startswith("BLANK"):
                last_line_index = index + first_line_index
                break

        lines = [line for line in lines[first_line_index:last_line_index] if not line.startswith("C")]


        if len(lines) > 0: 
            self._line = lines[0][:-1]
        else :
            self._line = " " * 80
        return self