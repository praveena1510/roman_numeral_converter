def convert_integer_to_roman_numerals(input_integer):
    roman_numeral = ""
    input_integer, roman_numeral = concatenate_roman_numeral(input_integer, roman_numeral)
    if input_integer >= 9:
        roman_numeral = roman_numeral + "IX"
        input_integer = input_integer - 9
    if input_integer >= 5:
        roman_numeral = roman_numeral + "V"
        input_integer = input_integer - 5
    if input_integer == 4:
        roman_numeral = roman_numeral + "IV"
        input_integer = input_integer - 4
    return roman_numeral + "I" * input_integer


def concatenate_roman_numeral(input_integer, roman_numeral):
    if input_integer >= 10:
        roman_numeral = roman_numeral + "X"
        input_integer = input_integer - 10
    return input_integer, roman_numeral

