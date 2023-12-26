import copy 
import subprocess
import concurrent.futures
import pyautogui
import os
import time

from miscellaneous import Miscellaneous
from models import Models
from branch import Branch
from switch import Switch
from source import Source
from output import Output
from plot import Plot

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

        end_line = "BLANK BRANCH\nBLANK SWITCH\nBLANK SOURCE\nBLANK OUTPUT\nBLANK PLOT\nBEGIN NEW DATA CASE\nBLANK\n"

        if len(self.models.models_codes) > 0:
            end_line = "BLANK MODELS\n" + end_line


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

        card_str += end_line

        return card_str

    def write_to_file(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.write())

    def copy(self):
        return copy.deepcopy(self)
    
    def from_file(self, file_name):

        # Get Lines 
        with open(file_name, "r") as f:
            lines = f.readlines()

        # If EXACT PHASOR EQUIVALENT\n is in the file, then exact phasor is true
        if "EXACT PHASOR EQUIVALENT\n" in lines:
            self.exact_phasor = True
            lines.remove("EXACT PHASOR EQUIVALENT\n")

        self.miscellaneous = self.miscellaneous.from_file(file_name)
        self.models = self.models.from_file(file_name)
        self.branch = self.branch.from_file(file_name)
        self.switch = self.switch.from_file(file_name)
        self.source = self.source.from_file(file_name)
        self.output = self.output.from_file(file_name)
        # self.plot = self.plot.from_file(file_name)

    def run_atp(
        self, 
        atp_path="C:/ATP/atpmingw/tpbig.exe", 
        output_path=os.getcwd(),
        atp_file_name="atp_input.atp",
        no_temp_file=True):
        
        # valid_alternatives = ["PY", "file_name", "DISK", "HELP", "GO", "KEY", "STOP", "BOTH", "DIR"]
        # if alternative not in valid_alternatives:
        #     raise ValueError(f"Alternative must be one of {valid_alternatives}")
        
        atp_path_folder = os.path.dirname(atp_path)
        os.chdir(atp_path_folder)

        

        self.write_to_file(atp_file_name)

        atp_input_path = os.path.join(os.getcwd(), atp_file_name)

        def run_atp_process(atp_path):
            # Run ATP 
            subprocess.run([atp_path])

        def send_input_process(atp_input_path):
            # Send the alternative to ATP
            pyautogui.write("BOTH")
            pyautogui.press("enter")




            # Send the input to ATP
            pyautogui.write(atp_input_path)
            pyautogui.press("enter")

            # Send the output to ATP
            pyautogui.write("-r")
            pyautogui.press("enter")

            #Finish atp 
            pyautogui.write("STOP")
            pyautogui.press("enter")




        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(run_atp_process, atp_path)
            executor.submit(send_input_process, atp_input_path)

            # concurrent.futures.wait([send_input_process, run_atp_process], return_when=concurrent.futures.ALL_COMPLETED)
         

        # put the output file in the output folder

        
        # see which files were modified in the last 10 seconds
        files = [f for f in os.listdir(atp_path_folder) if os.path.isfile(os.path.join(atp_path_folder, f))]
        files = [f for f in files if os.path.getmtime(os.path.join(atp_path_folder, f)) > time.time() - 10]

        if no_temp_file:
            files = [f for f in files if not f.endswith("tmp")]

        if not os.path.exists(output_path):
            os.mkdir(output_path)

        for file in files:
            # if file exists in the output folder, delete it and put the new one
            if os.path.exists(os.path.join(output_path, file)):
                os.remove(os.path.join(output_path, file))

            

            os.rename(os.path.join(atp_path_folder, file), os.path.join(output_path, file))

def read_atp(atp_path):
    card = ATPCard()
    card.from_file(atp_path)

    return card

def run_atp(
        atp_path="C:/ATP/atpmingw/tpbig.exe", 
        output_path=os.getcwd(),
        atp_file_name="atp_input.atp",
        no_temp_file=True
    ):

    card = ATPCard()
    card.from_file(atp_path)
    card.run_atp(atp_path, output_path, atp_file_name, no_temp_file)

