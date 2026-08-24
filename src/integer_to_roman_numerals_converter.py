def convert_integer_to_roman_numerals(input_integer):
    str = ""
    if input_integer>=5:
       str =  str + "V"
       input_integer= input_integer - 5
    if input_integer == 4:
        return "IV"
    return str + "I" * input_integer

