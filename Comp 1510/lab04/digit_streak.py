"""Lab 04 investigation: diagnose and repair the bug using test_digit_streak.py."""


def longest_digit_streak(text):
    """Return the length of the longest consecutive sequence of digits."""
    current_streak = 0
    longest_streak = 0
    index = 0
    while index < len(text):
        if text[index].isdigit():
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 0
        index += 1
    return longest_streak
