def convert_integer_to_roman_numerals(input_integer):
    roman_numerals = ""
    numeral_value_mapping = [(50, "L"), (40, "XL"),(10,"X"),(9, "IX"), (5, "V"),(4, "IV"), (1,"I")]
    for value, numeral in numeral_value_mapping:
        input_integer, roman_numerals = concatenate_roman_numeral(input_integer, roman_numerals, value, numeral)
    return roman_numerals


def concatenate_roman_numeral(input_integer, roman_numerals, value_of_numeral, numeral):
    while input_integer >= value_of_numeral:
        roman_numerals = roman_numerals + numeral
        input_integer = input_integer - value_of_numeral
    return input_integer, roman_numerals
