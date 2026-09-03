def convert_integer_to_roman_numerals(input_integer):
    roman_numerals = ""
    input_integer, roman_numerals = concatenate_roman_numeral(input_integer, roman_numerals, 10, "X")
    input_integer, roman_numerals = concatenate_roman_numeral(input_integer, roman_numerals, 9, "IX")
    input_integer, roman_numerals = concatenate_roman_numeral(input_integer, roman_numerals, 5, "V")
    input_integer, roman_numerals = concatenate_roman_numeral(input_integer, roman_numerals, 4, "IV")
    input_integer,roman_numerals = concatenate_roman_numeral (input_integer,roman_numerals,1,"I")
    return roman_numerals

def concatenate_roman_numeral(input_integer, roman_numerals, value_of_numeral, numeral):
    while input_integer >= value_of_numeral:
        roman_numerals = roman_numerals + numeral
        input_integer = input_integer - value_of_numeral
    return input_integer, roman_numerals

