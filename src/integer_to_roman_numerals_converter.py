def convert_integer_to_roman_numerals(input_integer):
    roman_numeral = ""
    if input_integer == 9:
        return "IX"
    if input_integer >= 5:
        roman_numeral = roman_numeral + "V"
        input_integer = input_integer - 5
    if input_integer == 4:
        return "IV"
    return roman_numeral + "I" * input_integer
