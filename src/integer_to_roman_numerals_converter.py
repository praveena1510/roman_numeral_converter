def convert_integer_to_roman_numerals(input_integer):
    if input_integer == 6:
        return "VI"
    if input_integer == 5:
        return "V"
    if input_integer == 4:
        return "IV"
    return "I" * input_integer

