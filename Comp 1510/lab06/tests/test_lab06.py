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


def test_top_words_returns_highest_scoring_subset():
    # Ordinary case: selects the top N words ordered from highest to lowest score.
    assert top_words(["QUIZ", "STAR", "JAZZ", "ACE"], 2) == ["JAZZ", "QUIZ"]


def test_top_words_zero_count_returns_empty_list():
    # Edge: requesting zero words returns an empty list.
    assert top_words(["QUIZ", "STAR"], 0) == []


def test_top_words_empty_list_returns_empty_list():
    # Edge: an empty word list returns an empty list even when count is positive.
    assert top_words([], 3) == []


def test_top_words_mixed_case_and_tied_scores():
    # Two rules at once: scoring is case-insensitive and tied scores are handled.
    assert top_words(["star", "quiz", "ARTS"], 2) == ["quiz", "star"]


# ----------------------------------------------------------------------------
# Question 2: letter_counts(word)
# Returns a dict mapping each uppercase letter in word to the number of
# times it appears. Case-insensitive.
# Write your tests below.
# ----------------------------------------------------------------------------


def test_letter_counts_repeated_uppercase_letters():
    # Ordinary case: counts multiple occurrences of letters in an uppercase word.
    assert letter_counts("BANANA") == {"B": 1, "A": 3, "N": 2}


def test_letter_counts_empty_word_returns_empty_dict():
    # Edge: an empty string produces an empty dictionary.
    assert letter_counts("") == {}


def test_letter_counts_mixed_case_duplicates_combine():
    # Two rules at once: converts lowercase to uppercase and sums duplicate letters.
    assert letter_counts("NeEdLe") == {"N": 1, "E": 3, "D": 1, "L": 1}


# ----------------------------------------------------------------------------
# Question 2: is_playable(word, rack)
# Returns True when the rack holds at least as many of each letter as the
# word needs. Case-insensitive.
# Write your tests below.
# ----------------------------------------------------------------------------


def test_is_playable_when_rack_has_needed_letters():
    # Ordinary case: rack contains all letters required to form the word.
    assert is_playable("STAR", "STARFISH") is True


def test_is_playable_false_when_letter_missing():
    # Ordinary case: rack is missing a required letter completely.
    assert is_playable("STAR", "STRFISH") is False


def test_is_playable_false_when_not_enough_duplicates():
    # Edge: rack has every unique letter needed, but not enough copies of 'E'.
    assert is_playable("NEED", "NEDDLY") is False


def test_is_playable_mixed_case_with_repeated_letters():
    # Two rules at once: ignores case and verifies duplicate letter quantities.
    assert is_playable("nEeD", "nEeDlE") is True


# ----------------------------------------------------------------------------
# Question 2: shared_letters(word, rack)
# Returns a set of the uppercase letters both strings have in common,
# ignoring how many times each appears. Case-insensitive.
# Write your tests below.
# ----------------------------------------------------------------------------


def test_shared_letters_finds_common_uppercase_letters():
    # Ordinary case: returns the set of unique letters present in both strings.
    assert shared_letters("NEED", "NEEDLE") == {"N", "E", "D"}


def test_shared_letters_disjoint_strings_return_empty_set():
    # Edge: strings with no letters in common return an empty set.
    assert shared_letters("CAT", "DOG") == set()


def test_shared_letters_mixed_case_and_duplicates_collapsed():
    # Two rules at once: normalizes case to uppercase and ignores letter frequency.
    assert shared_letters("bAnAnA", "nAb") == {"B", "A", "N"}


# ----------------------------------------------------------------------------
# Question 3: playable_words(rack, word_list)
# Returns a list of every word from word_list that is playable from rack.
# Write your tests below.
# ----------------------------------------------------------------------------


def test_playable_words_filters_valid_words():
    # Ordinary case: keeps only the words that can be formed from the rack.
    assert playable_words("AEINRST", ["STAR", "QUIZ", "TRAIN"]) == ["STAR", "TRAIN"]


def test_playable_words_none_playable_returns_empty_list():
    # Edge: returns an empty list when no words in the list can be formed.
    assert playable_words("XYZ", ["STAR", "TRAIN"]) == []


def test_playable_words_mixed_case_and_duplicate_requirements():
    # Two rules at once: matches words case-insensitively while enforcing letter counts.
    assert playable_words("nEeDlE", ["need", "DEER", "lend"]) == ["need", "lend"]


# ----------------------------------------------------------------------------
# Question 3: best_word(rack, word_list)
# Returns the highest-scoring playable word, or "" when no word is
# playable. Write your tests below.
# ----------------------------------------------------------------------------


def test_best_word_picks_highest_scoring_playable_word():
    # Ordinary case: returns the playable word with the highest point value.
    assert best_word("AEINRST", ["STAR", "RETAINS", "RAT"]) == "RETAINS"


def test_best_word_returns_empty_string_when_none_playable():
    # Edge: returns an empty string when playable_words finds no matches.
    assert best_word("XYZ", ["STAR", "TRAIN"]) == ""


def test_best_word_mixed_case_and_unplayable_high_scorer_ignored():
    # Two rules at once: ignores a higher-scoring unplayable word and handles mixed case.
    assert best_word("qUiZ", ["JAZZY", "quiz", "qi"]) == "quiz"