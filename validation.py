"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re


def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r'[aeiou]', string))


def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.search(r'^-?\d+$', string))


def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    return bool(re.search(r'^-?\d+/\d*[1-9]+\d*$', string))


def is_valid_time(string):
    """Return True iff the string represents a valid 24 hour time."""
    return bool(re.search(r'([0-1]\d|2[0-3]):[0-5]\d', string))


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    return bool(re.search(r'''
        (19|20) \d \d
        -
        ( 0[1-9] | 1[0-2] )
        -
        ( 0[1-9] | [12]\d | 3[01] )
    ''', string, re.VERBOSE))


def is_number(string):
    """Return True iff the string represents a decimal number."""
    return bool(re.search(r'^[-+]?(\d*\.?\d+|\d+\.\d*)$', string))


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
    return bool(re.search(r'^#([\da-f]{3}){1,2}$', string, re.IGNORECASE))
