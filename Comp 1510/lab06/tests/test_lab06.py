"""Starter tests for Lab 06 (wordgame.py).

Three example tests for word_score show the pattern: a descriptive name,
a comment naming the kind of case, and one assertion. Finish the suite by
writing tests for every function below. Keep one assertion per test
function, and run the tests in PyCharm: right-click tests/test_lab06.py
and choose Run 'pytest in test_lab06.py'. If PyCharm asks which test
runner to use, choose pytest.
"""

from wordgame import (
    word_score,
    top_words,
    letter_counts,
    is_playable,
    shared_letters,
    playable_words,
    best_word,
)


def test_mixed_values_are_summed():
    # Ordinary case: letters from different rows of the point table.
    assert word_score("BANANA") == 8


def test_empty_word_scores_zero():
    # Edge: a word with no letters still returns a number.
    assert word_score("") == 0


def test_lowercase_word_scores_the_same():
    # Two rules at once: scoring ignores case and letters differ in value.
    assert word_score("quiz") == 22


# ----------------------------------------------------------------------------
# Question 1: top_words(word_list, count)
# Returns the count highest-scoring words, ordered highest score first.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Question 2: letter_counts(word)
# Returns a dict mapping each uppercase letter in word to the number of
# times it appears. Case-insensitive.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Question 2: is_playable(word, rack)
# Returns True when the rack holds at least as many of each letter as the
# word needs. Case-insensitive.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Question 2: shared_letters(word, rack)
# Returns a set of the uppercase letters both strings have in common,
# ignoring how many times each appears. Case-insensitive.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Question 3: playable_words(rack, word_list)
# Returns a list of every word from word_list that is playable from rack.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Question 3: best_word(rack, word_list)
# Returns the highest-scoring playable word, or "" when no word is
# playable. Write your tests below.
# ----------------------------------------------------------------------------
