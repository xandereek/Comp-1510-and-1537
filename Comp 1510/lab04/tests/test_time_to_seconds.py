"""Tests for time_to_seconds (Lab 04, q2.py)."""

from q2 import time_to_seconds


def test_zero_time():
    # Boundary: midnight.
    assert time_to_seconds("00:00:00") == 0


def test_five_seconds_past_midnight():
    # Boundary: just past midnight.
    assert time_to_seconds("00:00:05") == 5


def test_one_hour_one_minute_eleven_seconds():
    # Partition: each field contributes its own multiplier.
    assert time_to_seconds("01:01:11") == 3671


def test_end_of_day():
    # Boundary: the last second of the day.
    assert time_to_seconds("23:59:59") == 86399
