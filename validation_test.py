"""Tests for validation exercises"""
import unittest


from validation import (has_vowel, is_integer, is_fraction, is_number,
                        is_hex_color, is_valid_date)


class HasVowelTests(unittest.TestCase):

    def test_rhythm(self):
        self.assertFalse(has_vowel("rhythm"))

    def test_exit(self):
        self.assertTrue(has_vowel("exit"))

    def test_no(self):
        self.assertTrue(has_vowel("no"))

    def test_yes(self):
        self.assertTrue(has_vowel("yes"))

    def test_fly(self):
        self.assertFalse(has_vowel("fly"))

    def test_symbols(self):
        self.assertFalse(has_vowel("%^&"))

    def test_empty(self):
        self.assertFalse(has_vowel(""))


class IsIntegerTests(unittest.TestCase):

    def test_single_digit(self):
        self.assertTrue(is_integer("5"))

    def test_leading_letter(self):
        self.assertFalse(is_integer("a5"))

    def test_trailing_letter(self):
        self.assertFalse(is_integer("5a"))

    def test_5000(self):
        self.assertTrue(is_integer("5000"))

    def test_leading_minus(self):
        self.assertTrue(is_integer("-999"))

    def test_leading_plus(self):
        self.assertFalse(is_integer("+999"))

    def test_leading_zero(self):
        self.assertTrue(is_integer("00"))

    def test_zero_decimal(self):
        self.assertFalse(is_integer("0.0"))

    def test_only_minus(self):
        self.assertFalse(is_integer("-"))

    def test_leading_space(self):
        self.assertFalse(is_integer(" 5"))

    def test_empty(self):
        self.assertFalse(is_integer(""))


class IsFractionTests(unittest.TestCase):

    def test_5000(self):
        self.assertFalse(is_fraction("5000"))

    def test_leading_minus(self):
        self.assertTrue(is_fraction("-999/1"))

    def test_leading_plus(self):
        self.assertFalse(is_fraction("+999/1"))

    def test_leading_zero_in_numerator(self):
        self.assertTrue(is_fraction("00/1"))

    def test_no_numerator(self):
        self.assertFalse(is_fraction("/5"))

    def test_no_denominator(self):
        self.assertFalse(is_fraction("5/"))

    def test_divide_by_zero(self):
        self.assertFalse(is_fraction("5/0"))

    def test_leading_zero_in_denominator(self):
        self.assertTrue(is_fraction("5/010"))

    def test_simple_fraction(self):
        self.assertTrue(is_fraction("5/105"))

    def test_with_spaces(self):
        self.assertFalse(is_fraction("5 / 1"))

    def test_empty(self):
        self.assertFalse(is_fraction(""))

    def test_leading_letter(self):
        self.assertFalse(is_fraction("a5"))

    def test_trailing_letter(self):
        self.assertFalse(is_fraction("5a"))


class IsNumberTests(unittest.TestCase):

    def test_5(self):
        self.assertTrue(is_number("5"))

    def test_5_point(self):
        self.assertTrue(is_number("5."))

    def test_point_5_point(self):
        self.assertFalse(is_number(".5."))

    def test_point_5(self):
        self.assertTrue(is_number(".5"))

    def test_leading_zero(self):
        self.assertTrue(is_number("01.5"))

    def test_negative(self):
        self.assertTrue(is_number("-123.859"))

    def test_two_decimals(self):
        self.assertFalse(is_number("-123.859."))

    def test_just_a_decimal(self):
        self.assertFalse(is_number("."))

    def test_leading_garbage(self):
        self.assertFalse(is_number("a5"))

    def test_trailing_garbage(self):
        self.assertFalse(is_number("5a"))


class IsHexColorTests(unittest.TestCase):

    def test_purple_short(self):
        self.assertTrue(is_hex_color("#639"))

    def test_four_digits(self):
        self.assertFalse(is_hex_color("#6349"))

    def test_five_digits(self):
        self.assertFalse(is_hex_color("#63459"))

    def test_dark_purple(self):
        self.assertTrue(is_hex_color("#634569"))

    def test_purple_long(self):
        self.assertTrue(is_hex_color("#663399"))

    def test_black(self):
        self.assertTrue(is_hex_color("#000000"))

    def test_two_digits(self):
        self.assertFalse(is_hex_color("#00"))

    def test_mixed_case(self):
        self.assertTrue(is_hex_color("#FFffFF"))

    def test_hex(self):
        self.assertTrue(is_hex_color("#decaff"))

    def test_invalid_character(self):
        self.assertFalse(is_hex_color("#decafz"))

    def test_no_octothorpe(self):
        self.assertFalse(is_hex_color("639"))

    def test_misplaced_octothorpe(self):
        self.assertFalse(is_hex_color("639#"))

    def test_leading_garbage(self):
        self.assertFalse(is_hex_color("a#639"))


class IsValidDateTests(unittest.TestCase):

    def test_this_year(self):
        self.assertTrue(is_valid_date("2016-01-02"))

    def test_1990(self):
        self.assertTrue(is_valid_date("1900-01-01"))

    def test_invalid_day(self):
        self.assertFalse(is_valid_date("2016-02-99"))

    def test_invalid_year(self):
        self.assertFalse(is_valid_date("20-02-20"))

    def test_invalid_month(self):
        self.assertFalse(is_valid_date("1980-30-05"))

    def test_leading_garbage(self):
        self.assertFalse(is_valid_date("12016-01-02"))

    def test_trailing_garbage(self):
        self.assertFalse(is_valid_date("2016-01-020"))


if __name__ == "__main__":
    raise SystemExit("No CLI for this file.  Run test.py instead.")
