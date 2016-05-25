"""
Substitution Exercises

These functions return a new altered version of the given string.

"""
import re


def get_extension(filename):
    """Return the file extension for a full file path."""
    return re.search(r'([^.]*)$', filename).group()


def normalize_jpeg(filename):
    """Return the filename with jpeg extensions normalized."""
    return re.sub(r'\.jpe?g$', r'.jpg', filename, flags=re.IGNORECASE)


def normalize_whitespace(string):
    """Replace all runs of whitespace with a single space."""
    return re.sub(r'\s+', r' ', string)


def compress_blank_lines(string, max_blanks):
    """Compress N or more empty lines into just N empty lines."""
    n = max_blanks + 1
    regex = r'\n{{{n},}}'.format(n=n)
    return re.sub(regex, '\n' * n, string)


def normalize_domain(string):
    """Normalize all instances of treyhunner.com URLs."""
    return re.sub(
        r'^https?://(www.)?treyhunner.com',
        r'https://treyhunner.com',
        string
    )


def convert_linebreaks(string):
    """Convert linebreaks to HTML."""
    string = re.sub(r'\n{2,}', '</p><p>', string)
    string = re.sub(r'\n', '<br>', string)
    return '<p>{}</p>'.format(string)
