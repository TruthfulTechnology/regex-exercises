Regular Expression Exercises
============================

These exercises accompany the Regular Expressions tutorial presented by `Trey Hunner`_ at PyCon 2017.


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
    Please select a function to test

    Functions that may be tested:
    [01]  has_vowel: Return True iff the string contains one or more vowels.
    [02]  is_integer: Return True iff the string represents a valid integer.
    [03]  is_fraction: Return True iff the string represents a valid fraction.
    [04]  is_valid_time: Return True iff the string represents a valid 24 hour time.
    [05]  is_valid_date: Return True iff the string represents a valid YYYY-MM-DD date.
    [06]  tetravocalic: Return a list of all words that have four consecutive vowels.
    [07]  hexadecimal: Return a list of all words consisting solely of the letters A to F.
    [08]  hexaconsonantal: Return a list of all words with six consecutive consonants.
    [09]  possible_words: Return possible word matches from a partial word.
    [10]  five_repeats: Return all words with at least five occurrences of the given letter.
    [11]  is_number: Return True iff the string represents a decimal number.
    [12]  is_hex_color: Return True iff the string represents an RGB hex color code.
    [13]  abbreviate: Return an acronym for the given phrase.
    [14]  palindrome5: Return a list of all five letter palindromes.
    [15]  double_double: Return words with a double repeated letter with one letter between.
    [16]  repeaters: Return words that consist of the same letters repeated two times.
    [17]  get_extension: Return the file extension for a full file path.
    [18]  normalize_jpeg: Return the filename with jpeg extensions normalized.
    [19]  normalize_whitespace: Replace all runs of whitespace with a single space.
    [20]  compress_blank_lines: Compress N or more empty lines into just N empty lines.
    [21]  normalize_domain: Normalize all instances of treyhunner.com URLs.
    [22]  convert_linebreaks: Convert linebreaks to HTML.
    [23]  have_all_vowels: Return all words at most 9 letters long that contain all vowels.
    [24]  no_repeats: Return all words with 10 or more letters and no repeating letters.
    [25]  to_pig_latin: Convert English phrase to Pig Latin.
    [26]  encode_ampersands: HTML-encode all & characters.
    [27]  camel_to_underscore: Convert camelCase strings to under_score.
    [28]  get_inline_links: Return a list of all inline links.
    [29]  find_broken_links: Return a list of all broken reference-style links.
    [30]  get_markdown_links: Return a list of all markdown links.

    What function would you like to test?

You will see a list of all exercises.  Note that each exercise has a name (e.g. ``has_vowel``) and a number (e.g. ``01``).

You can type in the name or number of the exercise to run it.


Solving an exercise
-------------------

To solve an exercise, navigate to the appropriate exercise module and find the exercise function.  For example:

.. code-block:: python

    def has_vowel(string):
        """Return True iff the string contains one or more vowels."""

Modify this function to return the expected result for any input.  Make sure to **use regular expressions** in your answer!


.. _trey hunner: http://treyhunner.com/
