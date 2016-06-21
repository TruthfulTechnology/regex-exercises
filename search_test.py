"""Tests for search exercises"""
import unittest


from search import (get_extension, hexadecimal, tetravocalic, hexaconsonantal,
                    five_repeats)


class GetExtensionTests(unittest.TestCase):

    def test_zip(self):
        self.assertEqual(get_extension('archive.zip'), 'zip')

    def test_jpeg(self):
        self.assertEqual(get_extension('image.jpeg'), 'jpeg')

    def test_xhtml(self):
        self.assertEqual(get_extension('index.xhtml'), 'xhtml')

    def test_gzipped_tarball(self):
        self.assertEqual(get_extension('archive.tar.gz'), 'gz')


class HexadecimalTests(unittest.TestCase):

    def test_cab(self):
        self.assertEqual(hexadecimal('cab'), ['cab'])

    def test_bed(self):
        self.assertEqual(hexadecimal('bed'), ['bed'])

    def test_cog(self):
        self.assertEqual(hexadecimal('cog'), [])

    def test_deed(self):
        self.assertEqual(hexadecimal('deed'), ['deed'])

    def test_sentence(self):
        sentence = "Hooligans defaced the cafe."
        self.assertEqual(
            hexadecimal(sentence.replace(' ', '\n')),
            ['defaced', 'cafe']
        )


class TetravocalicTests(unittest.TestCase):

    def test_three_vowels(self):
        self.assertEqual(tetravocalic("aei"), [])

    def test_four_vowels(self):
        self.assertEqual(tetravocalic("aeio"), ['aeio'])

    def test_five_vowels(self):
        self.assertEqual(tetravocalic("aeiou"), ['aeiou'])

    def test_non_consecutive(self):
        self.assertEqual(tetravocalic("aeixou"), [])

    def test_onomatopoeia(self):
        self.assertEqual(tetravocalic("onomatopoeia"), ['onomatopoeia'])

    def test_gooey(self):
        sentence = "A is gooey but B is gooier and C is gooiest"
        self.assertEqual(
            tetravocalic(sentence.replace(' ', '\n')),
            ['gooier', 'gooiest']
        )


class HexaconsonantalTests(unittest.TestCase):

    def test_borscht(self):
        self.assertEqual(hexaconsonantal("I\nlike\nborschts\n"), ['borschts'])

    def test_catchphrases(self):
        self.assertEqual(
            hexaconsonantal("favorite\ncatchphrases"),
            ['catchphrases']
        )

    def test_five_consonants(self):
        self.assertEqual(hexaconsonantal("touchscreen\nborscht"), [])


class FiveRepeatsTests(unittest.TestCase):

    def test_a(self):
        self.assertEqual(five_repeats('a'), ['abracadabra', 'abracadabras'])

    def test_b(self):
        self.assertEqual(five_repeats('b'), [])

    def test_c(self):
        self.assertEqual(five_repeats('c'), [])

    def test_d(self):
        self.assertEqual(five_repeats('d'), [])

    def test_e(self):
        words = five_repeats('e')
        self.assertIn('beekeeper', words)
        self.assertIn('interdependence', words)
        self.assertIn('peacekeeper', words)
        self.assertNotIn('peacekeeping', words)
        self.assertIn('reemergence', words)
        self.assertNotIn('speechlessness', words)


if __name__ == "__main__":
    raise SystemExit("No CLI for this file.  Run test.py instead.")
