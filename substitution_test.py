"""Tests for substitution exercises"""
from textwrap import dedent
import unittest


from substitution import (normalize_jpeg, normalize_whitespace,
                          compress_blank_lines, normalize_domain,
                          convert_linebreaks)


class NormalizeJPEGTests(unittest.TestCase):

    def test_jpeg(self):
        self.assertEqual(normalize_jpeg('avatar.jpeg'), 'avatar.jpg')

    def test_capital(self):
        self.assertEqual(normalize_jpeg('Avatar.JPEG'), 'Avatar.jpg')

    def test_mixed_case(self):
        self.assertEqual(normalize_jpeg('AVATAR.Jpg'), 'AVATAR.jpg')

    def test_gif(self):
        self.assertEqual(normalize_jpeg('avatar.gif'), 'avatar.gif')


class NormalizeWhitespaceTests(unittest.TestCase):

    def test_two_spaces(self):
        self.assertEqual(normalize_whitespace("hello  there"), "hello there")

    def test_poem(self):
        poem = dedent("""
            Hold fast to dreams
            For if dreams die
            Life is a broken-winged bird
            That cannot fly.

            Hold fast to dreams
            For when dreams go
            Life is a barren field
            Frozen with snow.
        """).strip()
        self.assertEqual(
            normalize_whitespace(poem),
            'Hold fast to dreams For if dreams die '
            'Life is a broken-winged bird That cannot fly. '
            'Hold fast to dreams For when dreams go '
            'Life is a barren field Frozen with snow.'
        )


class CompressBlankLinesTests(unittest.TestCase):

    def test_one_blank(self):
        self.assertEqual(
            compress_blank_lines("a\n\nb", max_blanks=1),
            'a\n\nb'
        )

    def test_no_blanks(self):
        self.assertEqual(
            compress_blank_lines("a\n\nb", max_blanks=0),
            'a\nb'
        )

    def test_two_blanks(self):
        self.assertEqual(
            compress_blank_lines("a\n\nb", max_blanks=2),
            'a\n\nb'
        )

    def test_many_blanks(self):
        self.assertEqual(
            compress_blank_lines("a\n\n\n\nb\n\n\nc", max_blanks=2),
            'a\n\n\nb\n\n\nc'
        )


class NormalizeDomainTests(unittest.TestCase):

    def test_http(self):
        self.assertEqual(
            normalize_domain("http://treyhunner.com/2015/12/"),
            'https://treyhunner.com/2015/12/'
        )

    def test_https(self):
        self.assertEqual(
            normalize_domain("https://treyhunner.com/2016/02/"),
            'https://treyhunner.com/2016/02/'
        )

    def test_www(self):
        self.assertEqual(
            normalize_domain("http://www.treyhunner.com/2015/11/"),
            'https://treyhunner.com/2015/11/'
        )

    def test_just_domain(self):
        self.assertEqual(
            normalize_domain("http://www.treyhunner.com"),
            'https://treyhunner.com'
        )

    def test_different_domain(self):
        self.assertEqual(
            normalize_domain("http://trey.in/give-a-talk"),
            'http://trey.in/give-a-talk'
        )


class ConvertLinebreaksTests(unittest.TestCase):

    def test_one_paragraph(self):
        self.assertEqual(
            convert_linebreaks("hello"),
            '<p>hello</p>'
        )

    def test_one_linebreak(self):
        self.assertEqual(
            convert_linebreaks("hello\nthere"),
            '<p>hello<br>there</p>'
        )

    def test_two_paragraphs(self):
        self.assertEqual(
            convert_linebreaks("hello\n\nthere"),
            '<p>hello</p><p>there</p>'
        )

    def test_two_paragraphs_with_break(self):
        self.assertEqual(
            convert_linebreaks("hello\nthere\n\nworld"),
            '<p>hello<br>there</p><p>world</p>'
        )


if __name__ == "__main__":
    raise SystemExit("No CLI for this file.  Run test.py instead.")
