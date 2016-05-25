"""
Lookahead Exercises

These functions could be made using lookaheads and/or lookbehinds.

"""
import re


with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def have_all_vowels(dictionary=dictionary):
    """Return all words at most 9 letters long that contain all vowels."""
    return re.findall(
        r'\b(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u).{1,9}\b',
        dictionary
    )


def no_repeats(dictionary=dictionary):
    """Return all words with 10 or more letters and no repeating letters."""
    return [
        m.group(0)
        for m in re.finditer(r'\b(?!.*(.).*\1).{10,}\b', dictionary)
    ]


def to_pig_latin(phrase):
    """Convert English phrase to Pig Latin."""
    PIG_LATIN_RE = re.compile(
        r'''\b
        ( (?: qu | [^aeiou\s] )* )
        ( \w* )
        \b''', re.VERBOSE)
    return PIG_LATIN_RE.sub(r'\2\1ay', phrase)


def encode_ampersands(phrase):
    """HTML-encode all & characters."""
    return re.sub(r'&(?![#\w]+;)', '&amp;', phrase)


def camel_to_underscore(camel_string):
    """Convert camelCase strings to under_score."""
    return re.sub(r'(.)([A-Z])(?=[^A-Z])', r'\1_\2', camel_string).lower()


INLINE_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \( (?P<url> .+?) \)
''', re.VERBOSE)


def get_inline_links(markdown):
    """Return a list of all inline links."""
    return [
        (m.group('text'), m.group('url'))
        for m in INLINE_RE.finditer(markdown)
    ]


BROKEN_RE1 = re.compile(r'''
    \[ (?P<text> .*?) \]
    \[ (?P<ref> .+?) \]
    (?!
        [\s\S]+
        \[ (?P=ref) \]: \s+
    )
''', re.VERBOSE | re.IGNORECASE)
BROKEN_RE2 = re.compile(r'''
    \[ (?P<ref> (?P<text> .+?)) \]
    \[ \]
    (?!
        [\s\S]+
        \[ (?P=text) \]: \s+
    )
''', re.VERBOSE | re.IGNORECASE)


def find_broken_links(markdown):
    """Return a list of all broken reference-style links."""
    return [
        (m.group('text'), m.group('ref'))
        for regex in (BROKEN_RE1, BROKEN_RE2)
        for m in regex.finditer(markdown)
    ]


REF1_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \[ (?P<ref> .+?) \]
    (?=
        [\s\S]+
        \[ (?P=ref) \]: \s+
        (?P<url> .+)
    )
''', re.VERBOSE | re.IGNORECASE)
REF2_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \[\]
    (?=
        [\s\S]+
        \[ (?P=text) \]: \s+
        (?P<url> .+)
    )
''', re.VERBOSE | re.IGNORECASE)
INLINE_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \( (?P<url> .+?) \)
''', re.VERBOSE)


def get_markdown_links(markdown):
    """Return a list of all markdown links."""
    results = (
        r.finditer(markdown)
        for r in (INLINE_RE, REF1_RE, REF2_RE)
    )
    return [
        (m.group('text'), m.group('url'))
        for matches in results
        for m in matches
    ]
