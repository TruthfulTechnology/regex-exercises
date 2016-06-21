"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re


with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension(filename):
    """Return the file extension for a full file path."""
    regex = r''  # FIXME put regular expression here
    return re.search(regex, filename).group(1)


def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    regex = r''  # FIXME put regular expression here
    return re.findall(regex, dictionary)


def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    regex = r''  # FIXME put regular expression here
    return re.findall(regex, dictionary)


def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    regex = r''  # FIXME put regular expression here
    return re.findall(regex, dictionary)


def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""
    regex = r''  # FIXME put regular expression here
    return re.findall(regex.format(letter), dictionary)
