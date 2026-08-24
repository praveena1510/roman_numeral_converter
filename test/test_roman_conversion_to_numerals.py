import unittest


def convert_numbers_to_roman_numeral(input_number):
    return "I"


class IntegerToRomanNumeral(unittest.TestCase):

    def test_converting_number_one_to_roman_numeral(self):
        self.assertEqual(convert_numbers_to_roman_numeral(1), "I")
