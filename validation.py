"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re


def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    regex = r''  # FIXME put regular expression here
    return bool(re.search(regex, string))


def is_integer(string):
    """Return True iff the string represents a valid integer."""
    regex = r''  # FIXME put regular expression here
    return bool(re.search(regex, string))


def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    regex = r''  # FIXME put regular expression here
    return bool(re.search(regex, string))


def is_number(string):
    """Return True iff the string represents a decimal number."""
    regex = r''  # FIXME put regular expression here
    return bool(re.search(regex, string))


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
    regex = r''  # FIXME put regular expression here
    return bool(re.search(regex, string, re.IGNORECASE))


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    # FIXME put verbose regular expression here
    regex = r'''
    '''
    return bool(re.search(regex, string, re.VERBOSE))
