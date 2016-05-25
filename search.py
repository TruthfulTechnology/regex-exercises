"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re


with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    return re.findall(r'\b.*[aeiou]{4}.*\b', dictionary)


def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    return re.findall(r'\b[a-f\d]+\b', dictionary)


def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    return re.findall(r'\b.*[^aeiouy\s]{6}.*\b', dictionary)


def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """
    pattern = r'\b{}\b'.format(partial_word.replace('_', '.'))
    return re.findall(pattern, dictionary, re.IGNORECASE)


def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""
    return re.findall(r'\b(?:.*{}.*){{5}}\b'.format(letter), dictionary)


def abbreviate(phrase):
    """Return an acronym for the given phrase."""
    return "".join(re.findall(r'(?:[a-z](?=[A-Z])|\b)(\w)', phrase)).upper()


def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""
    return [m.group(0) for m in re.finditer(r'\b(.)(.).\2\1\b', dictionary)]


def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """
    return [m.group(0) for m in re.finditer(r'\b.*(.)\1.\1\1.*\b', dictionary)]


def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
    return [m.group(0) for m in re.finditer(r'\b(.+)\1\b', dictionary)]
