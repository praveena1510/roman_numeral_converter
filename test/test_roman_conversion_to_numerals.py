import unittest

from parameterized import parameterized

from src.integer_to_roman_numerals_converter import convert_integer_to_roman_numerals


class IntegerToRomanNumeralsTest(unittest.TestCase):

    @parameterized.expand([
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (9, "IX"),
        (10, "X"),
        (11, "XI"),
        (14, "XIV"),
        (19, "XIX"),
        (20, "XX"),
        (40, "XL")
       ])
    def test_converting_integer_to_roman_numerals(self, input_integer: int, expected_roman_numeral: str):
        self.assertEqual(convert_integer_to_roman_numerals(input_integer), expected_roman_numeral)
