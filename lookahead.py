"""
Lookahead Exercises

These functions could be made using lookaheads and/or lookbehinds.

"""


with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def have_all_vowels(dictionary=dictionary):
    """Return all words at most 9 letters long that contain all vowels."""


def no_repeats(dictionary=dictionary):
    """Return all words with 10 or more letters and no repeating letters."""


def to_pig_latin(phrase):
    """Convert English phrase to Pig Latin."""


def encode_ampersands(phrase):
    """HTML-encode all & characters."""


def camel_to_underscore(camel_string):
    """Convert camelCase strings to under_score."""


def get_inline_links(markdown):
    """Return a list of all inline links."""


def find_broken_links(markdown):
    """Return a list of all broken reference-style links."""


def get_markdown_links(markdown):
    """Return a list of all markdown links."""
