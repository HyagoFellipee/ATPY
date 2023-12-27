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
    
def is_str_true(str, len):
    return str != " " * len and float(str) > 0

def scientific_to_decimal(scientific_str):

    decimal_str = "{:.20f}".format(float(scientific_str))
    decimal_str = decimal_str.rstrip('0').rstrip('.')
    return decimal_str

def cant_be_longer_message(name, max_len):
    return f"{name} can't be longer than {max_len} characters"

def valid_iout(iout, len):

    if iout == " " * len:
        return 0

    try:
        num_iout = float(iout)
    except ValueError:
        raise ValueError("Iout must be a number")
    
    valid_iout = [0, 1, 2, 3]

    if num_iout not in valid_iout:
        raise ValueError(f"Iout must be one of {valid_iout}")
    
    return num_iout
    