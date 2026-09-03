def convert_integer_to_roman_numerals(input_integer):
    roman_numerals = ""
    input_integer, roman_numerals = concatenate_roman_numeral(input_integer, roman_numerals)
    if input_integer >= 9:
        roman_numerals = roman_numerals + "IX"
        input_integer = input_integer - 9
    if input_integer >= 5:
        roman_numerals = roman_numerals + "V"
        input_integer = input_integer - 5
    if input_integer == 4:
        roman_numerals = roman_numerals + "IV"
        input_integer = input_integer - 4
    return roman_numerals + "I" * input_integer


def concatenate_roman_numeral(input_integer, roman_numerals):
    if input_integer >= 10:
        roman_numerals = roman_numerals + "X"
        input_integer = input_integer - 10
    return input_integer, roman_numerals

