#!/usr/bin/env python3
from collections import OrderedDict
import sys
import unittest


TESTS = OrderedDict([
    ('has_vowel', 'validation_test.HasVowelTests'),
    ('is_integer', 'validation_test.IsIntegerTests'),
    ('is_fraction', 'validation_test.IsFractionTests'),
    ('is_valid_time', 'validation_test.IsValidTimeTests'),
    ('is_valid_date', 'validation_test.IsValidDateTests'),
    ('tetravocalic', 'search_test.TetravocalicTests'),
    ('hexadecimal', 'search_test.HexadecimalTests'),
    ('hexaconsonantal', 'search_test.HexaconsonantalTests'),
    ('possible_words', 'search_test.PossibleWordsTests'),
    ('five_repeats', 'search_test.FiveRepeatsTests'),
    ('is_number', 'validation_test.IsNumberTests'),
    ('is_hex_color', 'validation_test.IsHexColorTests'),
    ('abbreviate', 'search_test.AbbreviateTests'),
    ('palindrome5', 'search_test.PalindromeTests'),
    ('double_double', 'search_test.DoubleDoubleTests'),
    ('repeaters', 'search_test.RepeatersTests'),
    ('get_extension', 'substitution_test.GetExtensionTests'),
    ('normalize_jpeg', 'substitution_test.NormalizeJPEGTests'),
    ('normalize_whitespace', 'substitution_test.NormalizeWhitespaceTests'),
    ('compress_blank_lines', 'substitution_test.CompressBlankLinesTests'),
    ('normalize_domain', 'substitution_test.NormalizeDomainTests'),
    ('convert_linebreaks', 'substitution_test.ConvertLinebreaksTests'),
    ('have_all_vowels', 'lookahead_test.HaveAllVowelsTests'),
    ('no_repeats', 'lookahead_test.NoRepeatsTests'),
    ('to_pig_latin', 'lookahead_test.ToPigLatinTests'),
    ('encode_ampersands', 'lookahead_test.EncodeAmpersandsTests'),
    ('camel_to_underscore', 'lookahead_test.CamelToUnderscoreTests'),
    ('get_inline_links', 'lookahead_test.GetInlineLinksTests'),
    ('find_broken_links', 'lookahead_test.FindBrokenLinksTests'),
    ('get_markdown_links', 'lookahead_test.GetMarkdownLinksTests'),
])


def get_function(func_id):
    """Return function name given a name or number."""
    try:
        n = int(func_id) - 1
    except ValueError:
        if func_id in TESTS:
            return func_id
    else:
        try:
            return list(TESTS.keys())[n]
        except IndexError:
            pass
    raise SystemExit("Function {} doesn't exist.".format(func_id))


def load_test(func_name):
    print("Testing function {}\n".format(func_name))
    tests = [unittest.defaultTestLoader.loadTestsFromName(TESTS[func_name])]
    test_suite = unittest.TestSuite(tests)
    unittest.TextTestRunner().run(test_suite)


def print_function_names():
    print("Functions that may be tested:")
    for n, (function_name, test_class_name) in enumerate(TESTS.items(), 1):
        module_name = test_class_name.split('.', 1)[0]
        function = getattr(__import__(module_name), function_name)
        print("[{n:02d}]  {name}: {doc}".format(
            n=n,
            name=function.__name__,
            doc=function.__doc__.strip().split('\n', 1)[0],
        ))


def get_function_name():
    print("Please select a function to test\n")
    print_function_names()
    print("")
    return input("What function would you like to test? ")


def main(*arguments):
    if not arguments:
        arguments = [get_function_name()]
    for arg in arguments:
        load_test(get_function(arg))


if __name__ == "__main__":
    main(*sys.argv[1:])
