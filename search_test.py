"""Tests for search exercises"""
import unittest


from search import (get_extension, hexadecimal, tetravocalic, hexaconsonantal,
                    possible_words, five_repeats, abbreviate, palindrome5,
                    double_double, repeaters)


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


class PossibleWordsTests(unittest.TestCase):

    def test_cistern(self):
        self.assertEqual(possible_words("CIS____"), ['cistern'])

    def test_axe(self):
        self.assertEqual(possible_words("_X_"), ['axe'])

    def test_c_t_(self):
        self.assertEqual(possible_words("c_t"), ['cat', 'cot', 'cut'])


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


class AbbreviateTests(unittest.TestCase):

    def test_gif(self):
        self.assertEqual(abbreviate('Graphics Interchange Format'), 'GIF')

    def test_faq(self):
        self.assertEqual(abbreviate('frequently asked questions'), 'FAQ')

    def test_css(self):
        self.assertEqual(abbreviate('cascading style sheets'), 'CSS')

    def test_cms(self):
        self.assertEqual(abbreviate('content management system'), 'CMS')

    def test_json(self):
        self.assertEqual(abbreviate('JavaScript Object Notation'), 'JSON')

    def test_html(self):
        self.assertEqual(abbreviate('HyperText Markup Language'), 'HTML')


class PalindromeTests(unittest.TestCase):

    def test_kayak(self):
        self.assertEqual(palindrome5('kayak'), ['kayak'])

    def test_partial(self):
        self.assertEqual(palindrome5('what were you referring to?'), [])

    def test_multiple(self):
        self.assertEqual(
            palindrome5('which level are you and what are your stats?'),
            ['level', 'stats']
        )

    def test_wrong_length(self):
        self.assertEqual(palindrome5('racecar driver doing a pullup'), [])


class DoubleDoubleTests(unittest.TestCase):

    def test_no_in_between(self):
        self.assertEqual(double_double('eeee'), [])

    def test_one_in_between(self):
        self.assertEqual(double_double('eexee'), ['eexee'])

    def test_two_in_between(self):
        self.assertEqual(double_double('eexxee'), [])

    def test_singles(self):
        self.assertEqual(double_double('aba'), [])

    def test_triples(self):
        self.assertEqual(double_double('aaabaaa'), ['aaabaaa'])

    def test_beekeeper(self):
        self.assertEqual(double_double('beekeeper'), ['beekeeper'])

    def test_two_words(self):
        words = 'Your freebees need more pizzazz.'.replace(' ', '\n')
        self.assertEqual(double_double(words), ['freebees', 'pizzazz'])

    def test_three_words(self):
        sentence = 'The granddaddy of all dispossessed squeegees.'
        self.assertEqual(
            double_double(sentence.replace(' ', '\n')),
            ['granddaddy', 'dispossessed', 'squeegees']
        )


class RepeatersTests(unittest.TestCase):

    def test_tutu(self):
        self.assertEqual(repeaters('tutu'), ['tutu'])

    def test_cancan(self):
        self.assertEqual(repeaters('cancan'), ['cancan'])

    def test_murmur(self):
        self.assertEqual(repeaters('murmur'), ['murmur'])

    def test_multiple(self):
        sentence = 'look at those froufrou hotshots'
        self.assertEqual(repeaters(sentence), ['froufrou', 'hotshots'])

    def test_whole_word(self):
        sentence = "gaga for bonbons"
        self.assertEqual(repeaters(sentence), ['gaga'])


if __name__ == "__main__":
    raise SystemExit("No CLI for this file.  Run test.py instead.")
