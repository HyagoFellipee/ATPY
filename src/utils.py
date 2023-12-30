def numeric_to_valid_str(numeric, spot_len, is_inductance = False, is_capacitance = False, ):

    if isinstance(numeric, float) or isinstance(numeric, int):

        if is_inductance:
            numeric = numeric / 1e-3

        if is_capacitance:
            numeric = numeric / 1e-6
        
        numeric = f"{numeric:.{spot_len}E}"
        
        if ('+' in numeric): 
            numeric = numeric.replace('+', '')

        
        splited = numeric.split('E')

        for chr in splited[1]: 
            if chr == '-':
                continue
            if chr == '0':
                splited[1] = splited[1].replace(chr, '', 1)
            else:
                break

        numeric = splited[0] + 'E' + splited[1] if splited[1] != '' else splited[0]

        e_index = numeric.index('E') if 'E' in numeric else len(numeric)

        while len(numeric) > spot_len or numeric[e_index - 1] == '0':
            numeric = numeric[:e_index - 1] + numeric[e_index:]
            e_index -= 1

        if numeric[-1] == '.':
            numeric = numeric[:-1]

        return numeric
    else:
        return numeric
    
def bool_to_valid_str(bool):
    if bool:
        return "1"
    else:
        return "0"
    
def is_str_true(str):
    if str.strip() == "0" or str.strip() == "":
        return False
    else:
        return True


def scientific_to_decimal(scientific_str):

    decimal_str = "{:.20f}".format(float(scientific_str))
    decimal_str = decimal_str.rstrip('0').rstrip('.')
    return decimal_str

def cant_be_longer_message(name, max_len):
    return f"{name} can't be longer than {max_len} characters"

def valid_iout(iout):

    if iout.strip() == "":
        return 0

    try:
        num_iout = int(iout)
    except ValueError:
        raise ValueError("Iout must be an integer")
    
    valid_iout = [0, 1, 2, 3]

    if num_iout not in valid_iout:
        raise ValueError(f"Iout must be one of {valid_iout}")
    
    return num_iout

def valid_itype(itype):

    if itype.strip() == "":
        return 0

    try:
        num_itype = int(itype)
    except ValueError:
        raise ValueError("Itype must be an integer")
    

    return num_itype

def valid_iline(iline):

    if iline.strip() == "":
        return 0

    try:
        num_iline = int(iline)
    except ValueError:
        raise ValueError("Iline must be an integer")
    
    valid_iline = [0, 1, 2]

    if num_iline not in valid_iline:
        raise ValueError(f"Iline must be one of {valid_iline}")
    
    return num_iline

def valid_ipose(ipose):

    if ipose.strip() == "":
        return 0

    try:
        num_ipose = int(ipose)
    except ValueError:
        raise ValueError("ipose must be an integer")
    

    return num_ipose 