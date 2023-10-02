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

        end_line = "BLANK MODELS\nBLANK BRANCH\nBLANK SWITCH\nBLANK SOURCE\nBLANK OUTPUT\nBLANK PLOT\nBEGIN NEW DATA CASE\nBLANK"

        card_str += init_line
        if self.exact_phasor:
            card_str += "EXACT PHASOR EQUIVALENT\n"

        card_str += self.miscellaneous.write()
        card_str += self.models.write()
        card_str += numbering_line
        card_str += self.branch.write()
        card_str += self.switch.write()
        card_str += self.source.write()
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
        if len(new_delta_t) > 8:
            raise ValueError("Delta t cant be longer than 8 characters long")
        
        new_delta_t = " " * (8 - len(new_delta_t)) + new_delta_t 
        

        self.first_line = new_delta_t + self.first_line[8:]
        

        self._delta_t = new_delta_t

    @property
    def t_max(self):
        return self._t_max
    
    @t_max.setter
    def t_max(self, new_t_max):
        if len(new_t_max) > 8:
            raise ValueError("T max cant be longer than 8 characters long")
        
        new_t_max = " " * (8 - len(new_t_max)) + new_t_max 
        
        self.first_line = self.first_line[0:8] + new_t_max + self.first_line[16:]

        self._t_max = new_t_max

    @property
    def x_opt(self):
        return self._x_opt
    
    @x_opt.setter
    def x_opt(self, new_x_opt):
        if len(new_x_opt) > 8:
            raise ValueError("X opt cant be longer than 8 characters long")
        
        new_x_opt = " " * (8 - len(new_x_opt)) + new_x_opt 
        
        self.first_line = self.first_line[0:16] + new_x_opt + self.first_line[24:]

        self._x_opt = new_x_opt
    
    @property
    def c_opt(self):
        return self._c_opt
    
    @c_opt.setter
    def c_opt(self, new_c_opt):
        if len(new_c_opt) > 8:
            raise ValueError("C opt cant be longer than 8 characters long")
        
        new_c_opt = " " * (8 - len(new_c_opt)) + new_c_opt 
        
        self.first_line = self.first_line[0:24] + new_c_opt + self.first_line[32:]

        self._c_opt = new_c_opt

    @property
    def epslin(self):
        return self._epslin
    
    @epslin.setter
    def epslin(self, new_epslin):
        if len(new_epslin) > 8:
            raise ValueError("Epslin cant be longer than 8 characters long")
        
        new_epslin = " " * (8 - len(new_epslin)) + new_epslin 
        
        self.first_line = self.first_line[0:32] + new_epslin + self.first_line[40:]

        self._epslin = new_epslin
    
    @property
    def tolmat(self):
        return self._tolmat
    
    @tolmat.setter
    def tolmat(self, new_tolmat):
        if len(new_tolmat) > 8:
            raise ValueError("Tolmat cant be longer than 8 characters long")
        
        new_tolmat = " " * (8 - len(new_tolmat)) + new_tolmat 
        
        self.first_line = self.first_line[0:40] + new_tolmat + self.first_line[48:]

        self._tolmat = new_tolmat
    
    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 8:
            raise ValueError("Tstart cant be longer than 8 characters long")
        
        new_tstart = " " * (8 - len(new_tstart)) + new_tstart 
        
        self.first_line = self.first_line[0:48] + new_tstart

        self._tstart = new_tstart

    @property
    def iout(self):
        return self._iout
    
    @iout.setter
    def iout(self, new_iout):
        if len(new_iout) > 8:
            raise ValueError("Iout cant be longer than 8 characters long")
        
        new_iout = " " * (8 - len(new_iout)) + new_iout 
        
        self.second_line = new_iout + self.second_line[8:]
        
        self._iout = new_iout

    @property
    def iplot(self):
        return self._iplot
    
    @iplot.setter
    def iplot(self, new_iplot):
        if len(new_iplot) > 8:
            raise ValueError("Iplot cant be longer than 8 characters long")
        
        new_iplot = " " * (8 - len(new_iplot)) + new_iplot 
        
        self.second_line = self.second_line[0:8] + new_iplot + self.second_line[16:]

        self._iplot = new_iplot

    @property
    def idoubl(self):
        return self._idoubl
    
    @idoubl.setter
    def idoubl(self, new_idoubl):
        if len(new_idoubl) > 8:
            raise ValueError("Idoubl cant be longer than 8 characters long")
        
        new_idoubl = " " * (8 - len(new_idoubl)) + new_idoubl 
        
        self.second_line = self.second_line[0:16] + new_idoubl + self.second_line[24:]

        self._idoubl = new_idoubl

    @property
    def kout(self):
        return self._kout
    
    @kout.setter
    def kout(self, new_kout):
        if len(new_kout) > 8:
            raise ValueError("Kout cant be longer than 8 characters long")
        
        new_kout = " " * (8 - len(new_kout)) + new_kout 
        
        self.second_line = self.second_line[0:24] + new_kout + self.second_line[32:]

        self._kout = new_kout

    @property
    def maxout(self):
        return self._maxout
    
    @maxout.setter
    def maxout(self, new_maxout):
        if len(new_maxout) > 8:
            raise ValueError("Maxout cant be longer than 8 characters long")
        
        new_maxout = " " * (8 - len(new_maxout)) + new_maxout 
        
        self.second_line = self.second_line[0:32] + new_maxout + self.second_line[40:]


        self._maxout = new_maxout
    
    @property
    def ipun(self):
        return self._ipun
    
    @ipun.setter
    def ipun(self, new_ipun):
        if len(new_ipun) > 8:
            raise ValueError("Ipun cant be longer than 8 characters long")
        
        new_ipun = " " * (8 - len(new_ipun)) + new_ipun 
        
        self.second_line = self.second_line[0:40] + new_ipun + self.second_line[48:]

        self._ipun = new_ipun

    @property
    def memsav(self):
        return self._memsav
    
    @memsav.setter
    def memsav(self, new_memsav):
        if len(new_memsav) > 8:
            raise ValueError("Memsav cant be longer than 8 characters long")
        
        new_memsav = " " * (8 - len(new_memsav)) + new_memsav 
        
        self.second_line = self.second_line[0:48] + new_memsav + self.second_line[56:]

        self._memsav = new_memsav

    @property
    def icat(self):
        return self._icat
    
    @icat.setter
    def icat(self, new_icat):
        if len(new_icat) > 8:
            raise ValueError("Icat cant be longer than 8 characters long")
        
        new_icat = " " * (8 - len(new_icat)) + new_icat 
        
        self.second_line = self.second_line[0:56] + new_icat + self.second_line[64:]

        self._icat = new_icat

    @property
    def nenerg(self):
        return self._nenerg
    
    @nenerg.setter
    def nenerg(self, new_nenerg):
        if len(new_nenerg) > 8:
            raise ValueError("Nenerg cant be longer than 8 characters long")
        
        new_nenerg = " " * (8 - len(new_nenerg)) + new_nenerg 
        
        self.second_line = self.second_line[0:64] + new_nenerg + self.second_line[72:]

        self._nenerg = new_nenerg

    @property
    def iprsup(self):
        return self._iprsup
    
    @iprsup.setter
    def iprsup(self, new_iprsup):
        if len(new_iprsup) > 8:
            raise ValueError("Iprsup cant be longer than 8 characters long")
        
        new_iprsup = " " * (8 - len(new_iprsup)) + new_iprsup 
        
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


        self.inputs = {}
        self.outputs = []
        self.records = []
        self.models_codes = []
        self.model_boxes = []



    def write(self):
        models_str = ""
        
        init_line = "/MODELS\nMODELS\n"


        models_str += init_line


        models_str += self.write_inputs()
        models_str += self.write_outputs()
        models_str += self.write_models_codes()
        models_str += self.write_model_boxes()
        models_str += self.write_records()

        end_line = "ENDMODELS\n"
        models_str += end_line

        return models_str

    def write_inputs(self):
        inputs_str = "INPUT\n"

        for identifier, input in self.inputs.items():
            inputs_str += f"  {identifier} " "{" + input + "}\n" 

        return inputs_str

    def write_outputs(self):
        outputs_str = "OUTPUT\n"

        for output in self.outputs:
            outputs_str += f"  {output}\n"
        
        return outputs_str

    def write_records(self):
        records_str = "RECORD\n"

        for record in self.records:
            records_str += f"  {record} AS {record}\n"

        return records_str

    def write_models_codes(self):
        models_codes_str = ""

        for model_code in self.models_codes:
            models_codes_str += model_code.write()+"\n"
        
        return models_codes_str

    def write_model_boxes(self):    
        model_boxes_str = ""
        for model_box in self.model_boxes:
            model_boxes_str += model_box.write()+"\n"
        
        return model_boxes_str

    def increment_identifier(self, identifier):
        # Increment the identifier by 1
        # The identifier is a str that starts at MM0001 and increments by 1 for each input
        
        # Get the number from the identifier
        number = int(identifier[2:])
        number += 1

        # Convert the number back to a string
        number = str(number)

        # Add the leading zeros back
        number = "0" * (4 - len(number)) + number

        # Add the MM back
        number = "MM" + number
        return number

    def add_inputs(self, inputs):

        self.inputs = {}


        ident = "MM0001"
        
        for input in inputs:

            self.inputs[ident] = input
            ident = self.increment_identifier(identifier=ident)

    def add_outputs(self, outputs):
        for output in outputs:
            if len(output) > 6:
                raise ValueError("Output cant be more than 6 characters long") 
            
            # adding blanks if necessary
            output = output + " " * (6 - len(output)) 
            self.outputs.append(output)

    def add_records(self, records):
        for record in records: 
            if len(record) > 6:
                raise ValueError("Record cant be more than 6 characters long") 
            
            # adding blanks if necessary
           
            record = record + " " * (6 - len(record))
            self.records.append(record)
    
    def add_model_codes(self, model_code):
        self.model_codes.append(model_code)

    def add_model_box(self, model_box):
        self.model_boxes.append(model_box)

class ModelCode:
    def __init__(self) -> None:
        self._code = ""
        self.name = ""
        self.datas = []
        self.inputs = []
        self.outputs = []
        
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, new_code):

        self._code = new_code
        self.datas = self.get_something_from_code(new_code, "DATA")
        self.inputs = self.get_something_from_code(new_code, "INPUT")
        self.outputs = self.get_something_from_code(new_code, "OUTPUT")

        self.name = self.get_name_from_code(new_code)

    def add_code(self, code_filename):
        with open(code_filename, "r") as f:
            self.code = f.read()

    def get_name_from_code(self, code):
        # The name is in the first line of the code
        line = code.split("\n")[0]

        # The name is the second word of the line
        return line.split(" ")[1]

    def get_something_from_code(self, code, something):
        
        # The code, if it has a something, starts with something like this:

        '''  
        something   
          Gain        {dflt:1}   --gain of filter
          FilterFreq  {dflt:800} --anti-aliasing filter frequency
          FilterOrder {dflt:2}   --Order of Butterworth filter 0..3
          ScaleFreq   {dflt:50}  --Base frequency for scaling. 0=no scale
        INPUT
        '''

        # So we need to get the data between something until the ident line goes back, that not necessarily a keyword

        # Split the code by lines
        lines = code.split("\n")

        # Get the index of the something line, if it exists
        something_index = -1
        for index, line in enumerate(lines):
            if line.startswith(something):
                something_index = index
                break

        if something_index == -1:
            # There is no something
            return []
        

        # find the index of the line that doesn't start with 2 spaces
        ident_index = something_index + 1
        while lines[ident_index].startswith("  "):
            ident_index += 1
        
        # Get the something
        something_lines = lines[something_index + 1: ident_index]
        somethings = []

        # I want to get the somethings, that is after the two first chars, and before the next space
        for line in something_lines: 
            line = line[2:]
            somethings.append(line[:line.index(" ")])

        return somethings

    def write(self):
        return self.code


class ModelBox:
    def __init__(self, model_code) -> None:
        
        self.name = ""
        self.inputs = {}
        self.outputs = {}
        self._datas = {}
        self.model_code = model_code


    @property
    def model_code(self):
        return self._model_code

    @model_code.setter
    def model_code(self, new_model_code):

        self.clean()

        if not isinstance(new_model_code, ModelCode):
            raise TypeError("Model code must be of type ModelCode")
        
        
        for input in new_model_code.inputs:
            self.inputs[input] = ""
        
        for output in new_model_code.outputs:
            self.outputs[output] = ""
        

        for data in new_model_code.datas:
            self.datas[data] = ""

        


        self._model_code = new_model_code

    def clean(self):
        self.inputs = {}
        self.outputs = {}
        self._datas = {}

    def write(self):
        model_box_str = ""

        first_line = f"USE {self.model_code.name} AS {self.name}\n"

        model_box_str += first_line

        inputs_str = "INPUT\n"
        model_box_str += inputs_str

        for input_key, input_value in self.inputs.items():
            model_box_str += f"  {input_key}:= {input_value}\n"

        datas_str = "DATA\n"

        model_box_str += datas_str

        for data_key, data_value in self.datas.items():
            model_box_str += f"  {data_key}:= {data_value}\n"

        outputs_str = "OUTPUT\n"

        model_box_str += outputs_str
        
        for output_key, output_value in self.outputs.items():
            model_box_str += f"  {output_value}:={output_key}\n"

        close_line = "ENDUSE"
        model_box_str += close_line
        return model_box_str

    def add_data(self, data_key, data_value):
        if data_key not in self.datas.keys():
            raise ValueError("Data key must be in the model code")
        
        if len(str(data_value)) > 8:
            raise ValueError("Data value cant be more than 8 characters long")
        
        # adding blanks if necessary

        data_value = " " * (8 - len(str(data_value))) + str(data_value) 

        self.datas[data_key] = str(data_value)

    @property 
    def datas(self):
        return self._datas
    
    @datas.setter
    def datas(self, new_datas):
        for data_key, data_value in new_datas.items():
            self.add_data(data_key, data_value)

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
    def __init__(self):
        self.init_line = "/SOURCE\n"
        self.comment_line = "C < n 1><>< Ampl.  >< Freq.  ><Phase/T0><   A1   ><   T1   >< TSTART >< TSTOP  >\n"
        
        self.sources = []

    def write(self):
        return self.init_line + self.comment_line+"".join([source.write() for source in self.sources])

    def add_source(self, source):
        if not isinstance(source, SourceElement):
            raise TypeError("sources must be of type SourceElement")
        self.sources.append(source)

class SourceElement:
    def __init__(self):
        type_str_len = 2
        name_str_len = 6
        param_str_len = 10
        blank_len = 40

        self._itype = " " * type_str_len
        self._name = " " * name_str_len
        self._st = " " * type_str_len
        self._amplitude = " " * param_str_len

        self._blank = " " * blank_len

        self._tstart = " " * param_str_len
        self._tstop = " " * param_str_len


    
class DCSource(SourceElement):
    def __init__(self):
        super().__init__()

        line_len = 80
        self._line = " " * line_len
        
        # def __str__(self):
        #     return f"Itype: {self._itype}, Name: {self._name}, St: {self._st}, Amplitude: {self._amplitude}, Tstart: {self._tstart}, Tstop: {self._tstop}"
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
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) != 6:
            raise ValueError("Name must be 6 characters long")
        
        self._line = self._line[0:2] + new_name + self._line[8:]
        self._name = new_name

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) != 2:
            raise ValueError("St must be 2 characters long")
        
        self._line = self._line[0:8] + new_st + self._line[10:]

        self._st = new_st

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) != 10:
            raise ValueError("Amplitude must be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude + self._line[20:]

        self._amplitude = new_amplitude

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 10:
            raise ValueError("Tstart must be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart + self._line[70:]

        self._tstart = new_tstart

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) != 10:
            raise ValueError("Tstop must be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop + self._line[80:]

        self._tstop = new_tstop

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) != 80:
            raise ValueError("Line must be 80 characters long")
        
        self._line = new_line

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]

class RampSource(SourceElement):
    def __init__(self):
        super().__init__()     
        line_len = 80
        self._line = " " * line_len

        self._time0 = " " * 10

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
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) != 6:
            raise ValueError("Name must be 6 characters long")
        
        self._line = self._line[0:2] + new_name + self._line[8:]

        self._name = new_name

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) != 2:
            raise ValueError("St must be 2 characters long")
        
        self._line = self._line[0:8] + new_st + self._line[10:]

        self._st = new_st

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) != 10:
            raise ValueError("Amplitude must be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude + self._line[20:]

        self._amplitude = new_amplitude

    @property
    def time0(self):
        return self._time0
    
    @time0.setter
    def time0(self, new_time0):
        if len(new_time0) != 10:
            raise ValueError("Time0 must be 10 characters long")
        
        self._line = self._line[0:30] + new_time0 + self._line[40:]

        self._time0 = new_time0

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 10:
            raise ValueError("Tstart must be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart + self._line[70:]

        self._tstart = new_tstart

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) != 10:
            raise ValueError("Tstop must be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop + self._line[80:]

        self._tstop = new_tstop

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) != 80:
            raise ValueError("Line must be 80 characters long")
        
        self._line = new_line

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._time0 = new_line[30:40]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]

class SlopeRampSource(SourceElement):
    def __init__ (self):
        super().__init__()
        line_len = 80
        self._line = " " * line_len

        self._time0 = " " * 10
        self._A1 = " " * 10
        self._time1 = " " * 10
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
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) != 6:
            raise ValueError("Name must be 6 characters long")
        
        self._line = self._line[0:2] + new_name + self._line[8:]

        self._name = new_name

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) != 2:
            raise ValueError("St must be 2 characters long")
        
        self._line = self._line[0:8] + new_st + self._line[10:]

        self._st = new_st

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) != 10:
            raise ValueError("Amplitude must be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude + self._line[20:]

        self._amplitude = new_amplitude

    @property
    def time0(self):
        return self._time0
    
    @time0.setter
    def time0(self, new_time0):
        if len(new_time0) != 10:
            raise ValueError("Time0 must be 10 characters long")
        
        self._line = self._line[0:30] + new_time0 + self._line[40:]

        self._time0 = new_time0

    @property
    def A1(self):
        return self._A1
    
    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) != 10:
            raise ValueError("A1 must be 10 characters long")
        
        self._line = self._line[0:40] + new_A1 + self._line[50:]

        self._A1 = new_A1
    
    @property
    def time1(self):
        return self._time1
    
    @time1.setter
    def time1(self, new_time1):
        if len(new_time1) != 10:
            raise ValueError("Time1 must be 10 characters long")
        
        self._line = self._line[0:50] + new_time1 + self._line[60:]

        self._time1 = new_time1

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 10:
            raise ValueError("Tstart must be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart + self._line[70:]

        self._tstart = new_tstart

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) != 10:
            raise ValueError("Tstop must be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop + self._line[80:]

        self._tstop = new_tstop

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) != 80:
            raise ValueError("Line must be 80 characters long")
        
        self._line = new_line

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._time0 = new_line[30:40]
        self._A1 = new_line[40:50]
        self._time1 = new_line[50:60]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]

class CosineSource(SourceElement):
    def __init__(self):
        super().__init__()
        line_len = 80
        self._line = " " * line_len

        self._frequency = " " * 10
        self._phase = " " * 10
        self._A1 = " " * 10

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
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) != 6:
            raise ValueError("Name must be 6 characters long")
        
        self._line = self._line[0:2] + new_name + self._line[8:]

        self._name = new_name

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) != 2:
            raise ValueError("St must be 2 characters long")
        
        self._line = self._line[0:8] + new_st + self._line[10:]

        self._st = new_st

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) != 10:
            raise ValueError("Amplitude must be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude + self._line[20:]

        self._amplitude = new_amplitude

    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, new_frequency):
        if len(new_frequency) != 10:
            raise ValueError("Frequency must be 10 characters long")
        
        self._line = self._line[0:20] + new_frequency + self._line[30:]

        self._frequency = new_frequency

    @property
    def phase(self):
        return self._phase
    
    @phase.setter
    def phase(self, new_phase):
        if len(new_phase) != 10:
            raise ValueError("Phase must be 10 characters long")
        
        self._line = self._line[0:30] + new_phase + self._line[40:]

        self._phase = new_phase

    @property
    def A1(self):
        return self._A1
    
    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) != 10:
            raise ValueError("A1 must be 10 characters long")
        
        self._line = self._line[0:40] + new_A1 + self._line[50:]

        self._A1 = new_A1

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 10:
            raise ValueError("Tstart must be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart + self._line[70:]

        self._tstart = new_tstart

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) != 10:
            raise ValueError("Tstop must be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop + self._line[80:]

        self._tstop = new_tstop

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) != 80:
            raise ValueError("Line must be 80 characters long")
        
        self._line = new_line

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._frequency = new_line[20:30]
        self._phase = new_line[30:40]
        self._A1 = new_line[40:50]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]

class HeidlerSource(SourceElement):
    def __init__(self):
        super().__init__()
        line_len = 80
        self._line = " " * line_len

        self._frequency = " " * 10
        self._phase = " " * 10
        self._A1 = " " * 10

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
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) != 6:
            raise ValueError("Name must be 6 characters long")
        
        self._line = self._line[0:2] + new_name + self._line[8:]

        self._name = new_name

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) != 2:
            raise ValueError("St must be 2 characters long")
        
        self._line = self._line[0:8] + new_st + self._line[10:]

        self._st = new_st

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) != 10:
            raise ValueError("Amplitude must be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude + self._line[20:]

        self._amplitude = new_amplitude

    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, new_frequency):
        if len(new_frequency) != 10:
            raise ValueError("Frequency must be 10 characters long")
        
        self._line = self._line[0:20] + new_frequency + self._line[30:]

        self._frequency = new_frequency

    @property
    def phase(self):
        return self._phase
    
    @phase.setter
    def phase(self, new_phase):
        if len(new_phase) != 10:
            raise ValueError("Phase must be 10 characters long")
        
        self._line = self._line[0:30] + new_phase + self._line[40:]

        self._phase = new_phase

    @property
    def A1(self):
        return self._A1
    
    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) != 10:
            raise ValueError("A1 must be 10 characters long")
        
        self._line = self._line[0:40] + new_A1 + self._line[50:]

        self._A1 = new_A1

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) != 10:
            raise ValueError("Tstart must be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart + self._line[70:]

        self._tstart = new_tstart

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) != 10:
            raise ValueError("Tstop must be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop + self._line[80:]

        self._tstop = new_tstop

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) != 80:
            raise ValueError("Line must be 80 characters long")
        
        self._line = new_line

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._frequency = new_line[20:30]
        self._phase = new_line[30:40]
        self._A1 = new_line[40:50]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]


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
        
    def add_vars(self, vars):
        # The user can put less than 13 vars
        # if he puts less, the rest will be filled with blanks

        if len(vars) > 13:
            raise ValueError("There can be at most 13 vars")
        
        # I have to make sure that the vars are 6 characters long, adding blanks if necessary

        for i in range(len(vars)):
            if len(vars[i]) != 6:
                vars[i] = vars[i] + " " * (6 - len(vars[i]))
        
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
        self.vars = [var + " " * (6 - len(var)) for var in self.vars]

    @property
    def vars(self):
        return self._vars
    
    @vars.setter
    def vars(self, new_vars):
        
        self._vars = self.add_vars(new_vars)

    

class Plot:
    def __init__(self) -> None:
        pass

