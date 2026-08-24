import unittest

from src.integer_to_roman_numerals_converter import convert_integer_to_roman_numerals


class IntegerToRomanNumeralsTest(unittest.TestCase):

    def test_converting_number_one_to_roman_numeral(self):
        self.assertEqual(convert_integer_to_roman_numerals(1), "I")

    def test_converting_number_two_to_roman_numeral(self):
       self.assertEqual(convert_integer_to_roman_numerals(2),"II")
