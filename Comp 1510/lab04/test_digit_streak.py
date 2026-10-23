"""Supplied tests for the Lab 04 investigation. Leave them unchanged."""

from digit_streak import longest_digit_streak


def test_empty_text():
    assert longest_digit_streak("") == 0


def test_internal_streak():
    assert longest_digit_streak("A123B4") == 3


def test_streak_at_end():
    assert longest_digit_streak("A123") == 3
