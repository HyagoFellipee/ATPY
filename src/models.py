import copy 

class Models:
    def __init__(self) -> None:


        self.inputs = {}
        self.outputs = []
        self.records = []
        self.models_codes = []
        self.model_boxes = []

    def copy(self):
        return copy.deepcopy(self)

    def write(self):

        if(len(self.inputs) == 0):
            return ""
        
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
            models_codes_str += model_code.write()
        
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

    def from_file(self, file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
        
        first_line_index = -1
        last_line_index = -1

        for index, line in enumerate(lines):
            if line.startswith("/MODELS"):
                first_line_index = index + 1
                break
        
        for index, line in enumerate(lines[first_line_index:]):
            if line.startswith("ENDMODELS"):
                last_line_index = index + first_line_index + 1
                break
        
        lines = [line for line in lines[first_line_index:last_line_index] if not line.startswith("C")]
        lines = [line[:-1] for line in lines]

        # Getting inputs from lines
        inputs = []

        first_input_index = -1
        last_input_index = -1

        for index, line in enumerate(lines):
            if line.startswith("INPUT"):
                first_input_index = index + 1
                break

        
        # INPUT ends when the line doesn't start with 2 spaces
        for index, line in enumerate(lines[first_input_index:]):
            if not line.startswith("  "):
                last_input_index = index + first_input_index
                break
        
        inputs_lines = lines[first_input_index:last_input_index]

        for line in inputs_lines:
            line = line[2:]
            
            # input is stored between { and }
            input = line[line.index("{") + 1: line.index("}")]
            inputs.append(input)
        
        if first_input_index != -1:
            self.add_inputs(inputs)

        # Getting outputs from lines
        outputs = []

        first_output_index = -1
        last_output_index = -1

        for index, line in enumerate(lines):
            if line.startswith("OUTPUT"):
                first_output_index = index + 1
                break
        
        # OUTPUT ends when the line doesn't start with 2 spaces

        for index, line in enumerate(lines[first_output_index:]):
            if not line.startswith("  "):
                last_output_index = index + first_output_index
                break
        
        outputs_lines = lines[first_output_index:last_output_index]

        for line in outputs_lines:
            line = line[2:]
            outputs.append(line)
        
        if first_output_index != -1:
            self.add_outputs(outputs)

        # Getting records from lines    
        records = []

        first_record_index = -1
        last_record_index = -1

        for index, line in enumerate(lines):
            if line.startswith("RECORD"):
                first_record_index = index + 1
                break
        
        # RECORD ends when the line doesn't start with 2 spaces

        for index, line in enumerate(lines[first_record_index:]):
            if not line.startswith("  "):
                last_record_index = index + first_record_index
                break

        records_lines = lines[first_record_index:last_record_index]
        

        for line in records_lines:
            line = line[2:]

            # record is stored until the first space
            record = line[:line.index(" ")]
            records.append(record)

        if first_record_index != -1:
            self.add_records(records)

        # Getting models codes from lines

        first_model_code_indices = []
        last_model_code_indices = []

        for index, line in enumerate(lines):
            # The model code starts with "MODEL " 
            if line.startswith("MODEL "):
                first_model_code_indices.append(index)

        for index, line in enumerate(lines):
            if line.startswith("ENDMODEL"):
                last_model_code_indices.append(index+1)

        for first_model_code_index, last_model_code_index in zip(first_model_code_indices, last_model_code_indices):
            model_code_lines = lines[first_model_code_index:last_model_code_index]
            model_code = ModelCode()
            
            model_code_str = ""
            # Create the string of the model code
            for line in model_code_lines:
                model_code_str += line + "\n"

            model_code.code = model_code_str
            self.models_codes.append(model_code)

        # Getting model boxes from lines

        first_model_box_indices = []
        last_model_box_indices = []

        for index, line in enumerate(lines):
            if line.startswith("USE"):
                first_model_box_indices.append(index)
        
        for index, line in enumerate(lines):
            if line.startswith("ENDUSE"):
                last_model_box_indices.append(index)

        for first_model_box_index, last_model_box_index in zip(first_model_box_indices, last_model_box_indices):
            

            model_box_lines = lines[first_model_box_index:last_model_box_index+1]
            
            #Get the name of the model code, that is after the USE keyword
            model_code_name = model_box_lines[0].split(" ")[1]


            #Get the model code with the same name
            
            model_code = [model_code for model_code in self.models_codes if model_code.name == model_code_name][0]
            

            model_box = ModelBox(model_code)
            
            #Get the name of the model box, that is after the AS keyword
            model_box.name = model_box_lines[0].split(" ")[3]


            # Get the inputs of the model box

            first_input_index = -1
            last_input_index = -1

            for index, line in enumerate(model_box_lines):
                if line.startswith("INPUT"):
                    first_input_index = index + 1
                    break
            
            # INPUT ends when the line doesn't start with 2 spaces
            for index, line in enumerate(model_box_lines[first_input_index:]):
                if not line.startswith("  "):
                    last_input_index = index + first_input_index
                    break
            
            inputs_lines = model_box_lines[first_input_index:last_input_index]

            for line in inputs_lines:
                line = line[2:]
                
                # input key is after the two first spaces, and before the =:
                input_key = line[:line.index(":=")]

                # input value is after the ":= " 
                input_value = line[line.index(":=") + 3:]

                model_box.inputs[input_key] = input_value
            
            # Get the datas of the model box

            first_input_index = -1
            last_input_index = -1

            for index, line in enumerate(model_box_lines):
                if line.startswith("DATA"):
                    first_input_index = index + 1
                    break
            
            # DATA ends when the line doesn't start with 2 spaces
            for index, line in enumerate(model_box_lines[first_input_index:]):
                if not line.startswith("  "):
                    last_input_index = index + first_input_index
                    break
            
            datas_lines = model_box_lines[first_input_index:last_input_index]

            for line in datas_lines:
                line = line[2:]
                
                # data key is after the two first spaces, and before the =:
                data_key = line[:line.index(":=")]

                # data value is after the ":= " 
                data_value = line[line.index(":=") + 3:]


                model_box.add_data(data_key, data_value)

            # Get the outputs of the model box

            first_output_index = -1
            last_output_index = -1

            for index, line in enumerate(model_box_lines):
                if line.startswith("OUTPUT"):
                    first_output_index = index + 1
                    break
            
            # OUTPUT ends when the line doesn't start with 2 spaces
            for index, line in enumerate(model_box_lines[first_output_index:]):
                if not line.startswith("  "):
                    last_output_index = index + first_output_index
                    break

            
            outputs_lines = model_box_lines[first_output_index:last_output_index]

            for line in outputs_lines:
                line = line[2:]
                
                # output key is after the two first spaces, and before the =:
                output_value = line[:line.index(":=")]

                # output value is after the ":= " 
                output_key = line[line.index(":=") + 2:]

                model_box.outputs[output_key] = output_value

            self.model_boxes.append(model_box)

        return self

class ModelCode:
    def __init__(self) -> None:
        self._code = ""
        self.name = ""
        self.datas = []
        self.inputs = []
        self.outputs = []
        
    def copy(self):
        return copy.deepcopy(self)
    
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
        line = code.split("\n")[0].upper()


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

        inputs_str = "INPUT\n" if len(self.inputs) > 0 else ""
        model_box_str += inputs_str

        for input_key, input_value in self.inputs.items():
            model_box_str += f"  {input_key}:= {input_value}\n"

        datas_str = "DATA\n" if len(self.datas) > 0 else ""

        model_box_str += datas_str

        for data_key, data_value in self.datas.items():
            model_box_str += f"  {data_key}:= {data_value}\n"

        outputs_str = "OUTPUT\n" if len(self.outputs) > 0 else ""

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
        data_value = str(data_value).ljust(8)

        self.datas[data_key] = data_value

    @property 
    def datas(self):
        return self._datas
    
    @datas.setter
    def datas(self, new_datas):
        for data_key, data_value in new_datas.items():
            self.add_data(data_key, data_value)

