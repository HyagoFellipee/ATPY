def numeric_to_valid_str(numeric, is_inductance = False, is_capacitance = False, spot_len = 6):

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