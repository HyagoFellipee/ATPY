import copy 
 
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

    def copy(self):
        return copy.deepcopy(self)
    
    def from_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        
        first_line_index = -1
        last_line_index = -1

        for index, line in enumerate(lines):
            if line.startswith("/SOURCE"):
                first_line_index = index + 1
                break
        
        for index, line in enumerate(lines[first_line_index:]):
            if line.startswith("/"):
                last_line_index = index + first_line_index
                break

        lines = [line for line in lines[first_line_index:last_line_index] if not line.startswith("C")]

        lines = [line[:-1] for line in lines]

        for line in lines:
            dc_source = DCSource()
            dc_source.line = line
            self.add_source(dc_source)
        
        return self
    
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

    def copy(self):
        return copy.deepcopy(self)

class DCSource(SourceElement):
    def __init__(self):
        super().__init__()

        line_len = 80
        self._line = " " * line_len
        
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
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 6:
            raise ValueError("Name can't be 6 characters long")
        
        self._line = self._line[0:2] + new_name.ljust(6) + self._line[8:]
        self._name = new_name.ljust(6)

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) > 2:
            raise ValueError("St can't be 2 characters long")
        
        self._line = self._line[0:8] + new_st.ljust(2) + self._line[10:]

        self._st = new_st.ljust(2)

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) > 10:
            raise ValueError("Amplitude can't be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude.ljust(10) + self._line[20:]

        self._amplitude = new_amplitude.ljust(10)

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 10:
            raise ValueError("Tstart can't be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart.ljust(10) + self._line[70:]

        self._tstart = new_tstart.ljust(10)

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) > 10:
            raise ValueError("Tstop can't be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop.ljust(10) + self._line[80:]

        self._tstop = new_tstop.ljust(10)

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than 80 characters long")
        
        self._line = new_line.ljust(80)

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
        if len(new_itype) > 2:
            raise ValueError("Itype can't be 2 characters long")
        
        self._line = new_itype.ljust(2) + self._line[2:]

        self._itype = new_itype.ljust(2)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 6:
            raise ValueError("Name can't be 6 characters long")
        
        self._line = self._line[0:2] + new_name.ljust(6) + self._line[8:]

        self._name = new_name.ljust(6)

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) > 2:
            raise ValueError("St can't be 2 characters long")
        
        self._line = self._line[0:8] + new_st.ljust(2) + self._line[10:]

        self._st = new_st.ljust(2)

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) > 10:
            raise ValueError("Amplitude can't be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude.ljust(10) + self._line[20:]

        self._amplitude = new_amplitude.ljust(10)

    @property
    def time0(self):
        return self._time0
    
    @time0.setter
    def time0(self, new_time0):
        if len(new_time0) > 10:
            raise ValueError("Time0 can't be 10 characters long")
        
        self._line = self._line[0:30] + new_time0.ljust(10) + self._line[40:]

        self._time0 = new_time0.ljust(10)

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 10:
            raise ValueError("Tstart can't be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart.ljust(10) + self._line[70:]

        self._tstart = new_tstart.ljust(10)

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) > 10:
            raise ValueError("Tstop can't be 10 characters long")
        
        self._line = self._line[0:70] + new_tstop.ljust(10) + self._line[80:]

        self._tstop = new_tstop.ljust(10)

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than 80 characters long")
        
        self._line = new_line.ljust(80)

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
        if len(new_itype) > 2:
            raise ValueError("Itype can't be 2 characters long")
        
        self._line = new_itype.ljust(2) + self._line[2:]

        self._itype = new_itype.ljust(2)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 6:
            raise ValueError("Name can't be 6 characters long")
        
        self._line = self._line[0:2] + new_name.ljust(6) + self._line[8:]

        self._name = new_name.ljust(6)

    @property
    def st(self):
        return self._st
    
    @st.setter
    def st(self, new_st):
        if len(new_st) > 2:
            raise ValueError("St can't be 2 characters long")
        
        self._line = self._line[0:8] + new_st.ljust(2) + self._line[10:]

        self._st = new_st.ljust(2)

    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) > 10:
            raise ValueError("Amplitude can't be 10 characters long")
        
        self._line = self._line[0:10] + new_amplitude.ljust(10) + self._line[20:]

        self._amplitude = new_amplitude.ljust(10)

    @property
    def time0(self):
        return self._time0
    
    @time0.setter
    def time0(self, new_time0):
        if len(new_time0) > 10:
            raise ValueError("Time0 can't be 10 characters long")
        
        self._line = self._line[0:30] + new_time0.ljust(10) + self._line[40:]

        self._time0 = new_time0.ljust(10)

    @property
    def A1(self):
        return self._A1
    
    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) > 10:
            raise ValueError("A1 can't be 10 characters long")
        
        self._line = self._line[0:40] + new_A1.ljust(10) + self._line[50:]

        self._A1 = new_A1.ljust(10)
    
    @property
    def time1(self):
        return self._time1
    
    @time1.setter
    def time1(self, new_time1):
        if len(new_time1) > 10:
            raise ValueError("Time1 can't be 10 characters long")
        
        self._line = self._line[0:50] + new_time1.ljust(10) + self._line[60:]

        self._time1 = new_time1.ljust(10)

    @property
    def tstart(self):
        return self._tstart
    
    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 10:
            raise ValueError("Tstart can't be 10 characters long")
        
        self._line = self._line[0:60] + new_tstart.ljust(10) + self._line[70:]

        self._tstart = new_tstart.ljust(10)

    @property
    def tstop(self):
        return self._tstop
    
    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) > 10:
            raise ValueError("Tstop can't be longer than 10 characters")
        
        self._line = self._line[0:70] + new_tstop.ljust(10) + self._line[80:]

        self._tstop = new_tstop.ljust(10)

    @property
    def line(self):
        return self._line
    
    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than 80 characters")
        
        self._line = new_line.ljust(80)

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
        if len(new_itype) > 2:
            raise ValueError("Itype can't be longer than 2 characters")
        
        self._line = new_itype.ljust(2) + self._line[2:]

        self._itype = new_itype.ljust(2)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 6:
            raise ValueError("Name can't be longer than 6 characters")

        self._line = self._line[0:2] + new_name.ljust(6) + self._line[8:]
        self._name = new_name.ljust(6)

    @property
    def st(self):
        return self._st

    @st.setter
    def st(self, new_st):
        if len(new_st) > 2:
            raise ValueError("St can't be longer than 2 characters")

        self._line = self._line[0:8] + new_st.ljust(2) + self._line[10:]
        self._st = new_st.ljust(2)

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) > 10:
            raise ValueError("Amplitude can't be longer than 10 characters")

        self._line = self._line[0:10] + new_amplitude.ljust(10) + self._line[20:]
        self._amplitude = new_amplitude.ljust(10)

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, new_frequency):
        if len(new_frequency) > 10:
            raise ValueError("Frequency can't be longer than 10 characters")

        self._line = self._line[0:20] + new_frequency.ljust(10) + self._line[30:]
        self._frequency = new_frequency.ljust(10)

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, new_phase):
        if len(new_phase) > 10:
            raise ValueError("Phase can't be longer than 10 characters")

        self._line = self._line[0:30] + new_phase.ljust(10) + self._line[40:]
        self._phase = new_phase.ljust(10)

    @property
    def A1(self):
        return self._A1

    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) > 10:
            raise ValueError("A1 can't be longer than 10 characters")

        self._line = self._line[0:40] + new_A1.ljust(10) + self._line[50:]
        self._A1 = new_A1.ljust(10)

    @property
    def tstart(self):
        return self._tstart

    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 10:
            raise ValueError("Tstart can't be longer than 10 characters")

        self._line = self._line[0:60] + new_tstart.ljust(10) + self._line[70:]
        self._tstart = new_tstart.ljust(10)

    @property
    def tstop(self):
        return self._tstop

    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) > 10:
            raise ValueError("Tstop can't be longer than 10 characters")

        self._line = self._line[0:70] + new_tstop.ljust(10) + self._line[80:]
        self._tstop = new_tstop.ljust(10)

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than 80 characters")

        self._line = new_line.ljust(80)

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._frequency = new_line[20:30]
        self._phase = new_line[30:40]
        self._A1 = new_line[40:50]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]

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
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 6:
            raise ValueError("Name can't be longer than 6 characters")

        self._line = self._line[0:2] + new_name.ljust(6) + self._line[8:]
        self._name = new_name.ljust(6)

    @property
    def st(self):
        return self._st

    @st.setter
    def st(self, new_st):
        if len(new_st) > 2:
            raise ValueError("St can't be longer than 2 characters")

        self._line = self._line[0:8] + new_st.ljust(2) + self._line[10:]
        self._st = new_st.ljust(2)

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) > 10:
            raise ValueError("Amplitude can't be longer than 10 characters")

        self._line = self._line[0:10] + new_amplitude.ljust(10) + self._line[20:]
        self._amplitude = new_amplitude.ljust(10)

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, new_frequency):
        if len(new_frequency) > 10:
            raise ValueError("Frequency can't be longer than 10 characters")

        self._line = self._line[0:20] + new_frequency.ljust(10) + self._line[30:]
        self._frequency = new_frequency.ljust(10)

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, new_phase):
        if len(new_phase) > 10:
            raise ValueError("Phase can't be longer than 10 characters")

        self._line = self._line[0:30] + new_phase.ljust(10) + self._line[40:]
        self._phase = new_phase.ljust(10)

    @property
    def A1(self):
        return self._A1

    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) > 10:
            raise ValueError("A1 can't be longer than 10 characters")

        self._line = self._line[0:40] + new_A1.ljust(10) + self._line[50:]
        self._A1 = new_A1.ljust(10)

    @property
    def tstart(self):
        return self._tstart

    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 10:
            raise ValueError("Tstart can't be longer than 10 characters")

        self._line = self._line[0:60] + new_tstart.ljust(10) + self._line[70:]
        self._tstart = new_tstart.ljust(10)

    @property
    def tstop(self):
        return self._tstop

    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) > 10:
            raise ValueError("Tstop can't be longer than 10 characters")

        self._line = self._line[0:70] + new_tstop.ljust(10) + self._line[80:]
        self._tstop = new_tstop.ljust(10)

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than 80 characters")

        self._line = new_line.ljust(80)

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
        if len(new_itype) > 2:
            raise ValueError("Itype can't be longer than 2 characters")

        self._line = new_itype.ljust(2) + self._line[2:]
        self._itype = new_itype.ljust(2)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 6:
            raise ValueError("Name can't be longer than 6 characters")

        self._line = self._line[0:2] + new_name.ljust(6) + self._line[8:]
        self._name = new_name.ljust(6)

    @property
    def st(self):
        return self._st

    @st.setter
    def st(self, new_st):
        if len(new_st) > 2:
            raise ValueError("St can't be longer than 2 characters")

        self._line = self._line[0:8] + new_st.ljust(2) + self._line[10:]
        self._st = new_st.ljust(2)

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, new_amplitude):
        if len(new_amplitude) > 10:
            raise ValueError("Amplitude can't be longer than 10 characters")

        self._line = self._line[0:10] + new_amplitude.ljust(10) + self._line[20:]
        self._amplitude = new_amplitude.ljust(10)

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, new_frequency):
        if len(new_frequency) > 10:
            raise ValueError("Frequency can't be longer than 10 characters")

        self._line = self._line[0:20] + new_frequency.ljust(10) + self._line[30:]
        self._frequency = new_frequency.ljust(10)

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, new_phase):
        if len(new_phase) > 10:
            raise ValueError("Phase can't be longer than 10 characters")

        self._line = self._line[0:30] + new_phase.ljust(10) + self._line[40:]
        self._phase = new_phase.ljust(10)

    @property
    def A1(self):
        return self._A1

    @A1.setter
    def A1(self, new_A1):
        if len(new_A1) > 10:
            raise ValueError("A1 can't be longer than 10 characters")

        self._line = self._line[0:40] + new_A1.ljust(10) + self._line[50:]
        self._A1 = new_A1.ljust(10)

    @property
    def tstart(self):
        return self._tstart

    @tstart.setter
    def tstart(self, new_tstart):
        if len(new_tstart) > 10:
            raise ValueError("Tstart can't be longer than 10 characters")

        self._line = self._line[0:60] + new_tstart.ljust(10) + self._line[70:]
        self._tstart = new_tstart.ljust(10)

    @property
    def tstop(self):
        return self._tstop

    @tstop.setter
    def tstop(self, new_tstop):
        if len(new_tstop) > 10:
            raise ValueError("Tstop can't be longer than 10 characters")

        self._line = self._line[0:70] + new_tstop.ljust(10) + self._line[80:]
        self._tstop = new_tstop.ljust(10)

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, new_line):
        if len(new_line) > 80:
            raise ValueError("Line can't be longer than 80 characters")

        self._line = new_line.ljust(80)

        self._itype = new_line[0:2]
        self._name = new_line[2:8]
        self._st = new_line[8:10]
        self._amplitude = new_line[10:20]
        self._frequency = new_line[20:30]
        self._phase = new_line[30:40]
        self._A1 = new_line[40:50]
        self._tstart = new_line[60:70]
        self._tstop = new_line[70:80]
