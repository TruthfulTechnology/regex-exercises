Regular Expression Exercises
============================

These exercises accompany the Regular Expressions tutorial presented by `Trey Hunner`_ at Open Source Bridge 2016.


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
    [04]  get_extension: Return the file extension for a full file path.
    [05]  hexadecimal: Return a list of all words consisting solely of the letters A to F.
    [06]  tetravocalic: Return a list of all words that have four consecutive vowels.
    [07]  hexaconsonantal: Return a list of all words with six consecutive consonants.
    [08]  five_repeats: Return all words with at least five occurrences of the given letter.
    [09]  is_number: Return True iff the string represents a decimal number.
    [10]  is_hex_color: Return True iff the string represents an RGB hex color code.
    [11]  is_valid_date: Return True iff the string represents a valid YYYY-MM-DD date.

    What function would you like to test?

You will see a list of all exercises.  Note that each exercise has a name (e.g. ``has_vowel``) and a number (e.g. ``01``).

You can type in the name or number of the exercise to run it.


Solving an exercise
-------------------

To solve an exercise, navigate to the appropriate exercise module and find the exercise function.  For example:

.. code-block:: python

    def has_vowel(string):
        """Return True iff the string contains one or more vowels."""
        regex = r''  # FIXME put regular expression here
        return bool(re.search(regex, string))


Modify this function to return the expected result for any input.  Make sure to **use regular expressions** in your answer!


.. _trey hunner: http://treyhunner.com/
