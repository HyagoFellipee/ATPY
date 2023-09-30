class CardGenerator: 
    def __init__(self):
        self.miscelanous = Miscelanous()
        self.models = Models() 
        self.branch = Branch() 
        self.switch = Switch()
        self.source = Source()
        self.output = Output()
        self.plot = Plot()

        self.high_precison = False 
        self.fixed_format = True 


class Miscelanous:
    def __init__(self) -> None:

        self.comment_line = "C  dT  >< Tmax >< Xopt >< Copt ><Epsiln>"

        # First Miscelanous line 
        self.delta_t = "   1.E-6"
        self.t_max   = "    .001"
        self.x_opt   = "        "  
        self.c_opt   = "        "  
        self.epslin  = "        "  
        self.tolmat  = "        "  
        self.tstart  = "        "  

        self.first_line = f"{self.delta_t}{self.t_max}{self.x_opt}{self.c_opt}{self.epslin}{self.tolmat}{self.tstart}"

        # Second Miscelanous line
        self.iout   = "     500"
        self.iplot  = "       1"
        self.idoubl = "       1"
        self.kout   = "       1"
        self.maxout = "       1"
        self.ipun   = "       0"
        self.memsav = "       0"
        self.icat   = "       1"
        self.nenerg = "       0"
        self.iprsup = "        "

        self.second_line = f"{self.iout}{self.iplot}{self.idoubl}{self.kout}{self.maxout}{self.ipun}{self.memsav}{self.icat}{self.nenerg}{self.iprsup}"

    def write(self): 
        return f"{self.comment_line}\n{self.first_line}\n{self.second_line}\n"


class Models:
    def __init__(self) -> None:
        pass

class Branch:
    def __init__(self) -> None:
        pass

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

