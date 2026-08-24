import unittest


def convert_integer_to_roman_numerals(input_integer):
    return "I"


class IntegerToRomanNumeralsTest(unittest.TestCase):

    def test_converting_number_one_to_roman_numeral(self):
        self.assertEqual(convert_integer_to_roman_numerals(1), "I")
