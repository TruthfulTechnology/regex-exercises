"""Tests for lookahead exercises"""
from textwrap import dedent
import unittest


from lookahead import (have_all_vowels, no_repeats, encode_ampersands,
                       to_pig_latin, camel_to_underscore,
                       find_broken_links, get_inline_links, get_markdown_links)


class HaveAllVowelsTests(unittest.TestCase):

    def test_vowels_in_order(self):
        self.assertEqual(have_all_vowels("facetious"), ['facetious'])

    def test_vowels_out_of_order(self):
        self.assertEqual(have_all_vowels("euphoria"), ['euphoria'])

    def test_multiple_words(self):
        words = "Let's have a dialogue about education.".replace(" ", "\n")
        self.assertEqual(have_all_vowels(words), ['dialogue', 'education'])

    def test_too_long(self):
        self.assertEqual(have_all_vowels('educational'), [])


class NoRepeatsTests(unittest.TestCase):

    def test_background(self):
        self.assertEqual(no_repeats("background"), ['background'])

    def test_multiple(self):
        words = "the\ntambourines\nnefariously\nclamouring\neverywhere"
        self.assertEqual(
            no_repeats(words),
            ['tambourines', 'nefariously', 'clamouring']
        )

    def test_too_short(self):
        self.assertEqual(no_repeats('authorize'), [])


class EncodeAmpersandsTests(unittest.TestCase):

    def test_a_and_w(self):
        self.assertEqual(encode_ampersands("A&W"), "A&amp;W")

    def test_encoded_ampersand(self):
        self.assertEqual(encode_ampersands("&amp;"), "&amp;")

    def test_copyright(self):
        self.assertEqual(encode_ampersands("&copy;"), "&copy;")

    def test_numeric_encoding(self):
        self.assertEqual(encode_ampersands("&#38;"), "&#38;")

    def test_whole_sentence(self):
        sentence = "This &amp; that & that &#38; this."
        encoded = "This &amp; that &amp; that &#38; this."
        self.assertEqual(encode_ampersands(sentence), encoded)


class ToPigLatinTests(unittest.TestCase):

    def test_apple(self):
        self.assertEqual(to_pig_latin("apple"), 'appleay')

    def test_eggs(self):
        self.assertEqual(to_pig_latin("eggs"), 'eggsay')

    def test_pig(self):
        self.assertEqual(to_pig_latin("pig"), 'igpay')

    def test_trust(self):
        self.assertEqual(to_pig_latin("trust"), 'usttray')

    def test_quack(self):
        self.assertEqual(to_pig_latin("quack"), 'ackquay')

    def test_squeak(self):
        self.assertEqual(to_pig_latin("squeak"), 'eaksquay')

    def test_enqeue(self):
        self.assertEqual(to_pig_latin("enqueue"), 'enqueueay')

    def test_sequoia(self):
        self.assertEqual(to_pig_latin("sequoia"), 'equoiasay')


class CamelToUnderscoreTests(unittest.TestCase):

    def test_index_of(self):
        self.assertEqual(camel_to_underscore("indexOf"), "index_of")

    def test_to_lowercase(self):
        self.assertEqual(camel_to_underscore("toLowerCase"), "to_lower_case")

    def test_xml(self):
        self.assertEqual(camel_to_underscore("XML"), "xml")

    def test_http_client(self):
        self.assertEqual(camel_to_underscore("HTTPClient"), "http_client")

    def test_xml_http_request(self):
        self.assertEqual(
            camel_to_underscore("XMLHttpRequest"),
            "xml_http_request"
        )


class GetInlineLinksTests(unittest.TestCase):

    def test_multiple_links(self):
        markdown = dedent("""
            [Python](https://www.python.org)
            [Google](https://www.google.com)""")
        self.assertEqual(
            get_inline_links(markdown),
            [('Python', 'https://www.python.org'),
             ('Google', 'https://www.google.com')]
        )


class FindBrokenLinksTests(unittest.TestCase):

    def test_multiple_links(self):
        markdown = dedent("""
            [working link][Python]
            [broken link][Google]
            [python]: https://www.python.org/""")
        self.assertEqual(
            find_broken_links(markdown),
            [('broken link', 'Google')]
        )

    def test_implicit_links(self):
        markdown = dedent("""
            [Python][]
            [Google][]
            [python]: https://www.python.org/""")
        self.assertEqual(
            find_broken_links(markdown),
            [('Google', 'Google')]
        )


class GetMarkdownLinksTests(unittest.TestCase):

    def test_multiple_links(self):
        markdown = dedent("""
            [Python](https://www.python.org)
            [Google][]
            [Another link][example]
            [google]: https://www.google.com
            [example]: http://example.com""")
        self.assertEqual(
            set(get_markdown_links(markdown)),
            {('Python', 'https://www.python.org'),
             ('Google', 'https://www.google.com'),
             ('Another link', 'http://example.com')}
        )


if __name__ == "__main__":
    raise SystemExit("No CLI for this file.  Run test.py instead.")
