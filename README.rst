Regular Expression Exercises
============================

These exercises accompany the Regular Expressions tutorial presented by `Trey Hunner`_ at PyTennessee 2017.


Testing an exercise by name
---------------------------

.. code-block:: bash

    $ python test.py has_vowel
    Testing function has_vowel

    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.000s

    OK

You will see ``OK`` if your code passes the tests and ``FAILED`` if your code fails one or more tests.

Forgot the exercise name?
-------------------------

If you're not sure of the function name for your exercise, just run the ``test.py`` file without any arguments to see a list of all exercise names:

.. code-block:: bash

    $ python test.py
    Please select a thing to test

    lookahead:

    camel_to_underscore: Convert camelCase strings to under_score.
    encode_ampersands: HTML-encode all & characters.
    find_broken_links: Return a list of all broken reference-style links.
    get_inline_links: Return a list of all inline links.
    get_markdown_links: Return a list of all markdown links.
    have_all_vowels: Return all words at most 9 letters long that contain all vowels.
    no_repeats: Return all words with 10 or more letters and no repeating letters.
    to_pig_latin: Convert English phrase to Pig Latin.

    search:

    abbreviate: Return an acronym for the given phrase.
    count_numbers: Return the count of all numbers in a given string.
    count_punctuation: Return count of all punctuation characters in given string.
    double_double: Return words with a double repeated letter with one letter between.
    five_repeats: Return all words with at least five occurrences of the given letter.
    hexaconsonantal: Return a list of all words with six consecutive consonants.
    hexadecimal: Return a list of all words consisting solely of the letters A to F.
    palindrome5: Return a list of all five letter palindromes.
    possible_words: Return possible word matches from a partial word.
    repeaters: Return words that consist of the same letters repeated two times.
    tetravocalic: Return a list of all words that have four consecutive vowels.

    validation:

    has_vowel: Return True iff the string contains one or more vowels.
    is_fraction: Return True iff the string represents a valid fraction.
    is_hex_color: Return True iff the string represents an RGB hex color code.
    is_integer: Return True iff the string represents a valid integer.
    is_number: Return True iff the string represents a decimal number.
    is_valid_date: Return True iff the string represents a valid YYYY-MM-DD date.
    is_valid_time: Return True iff the string represents a valid 24 hour time.

    substitution:

    compress_blank_lines: Compress N or more empty lines into just N empty lines.
    convert_linebreaks: Convert linebreaks to HTML.
    get_extension: Return the file extension for a full file path.
    normalize_domain: Normalize all instances of treyhunner.com URLs.
    normalize_jpeg: Return the filename with jpeg extensions normalized.
    normalize_whitespace: Replace all runs of whitespace with a single space.

You will see a list of all exercises grouped by the module they live in.  Note that each exercise has a name (e.g. ``has_vowel``).  You can type in the name of the exercise to run it.


Solving an exercise
-------------------

To solve an exercise, navigate to the appropriate exercise module and find the exercise function.  For example:

.. code-block:: python

    def has_vowel(string):
        """Return True iff the string contains one or more vowels."""

Modify this function to return the expected result for any input.  Make sure to **use regular expressions** in your answer!


.. _trey hunner: http://truthful.technology
