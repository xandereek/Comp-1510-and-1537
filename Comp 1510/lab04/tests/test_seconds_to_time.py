"""Tests for seconds_to_time (Lab 04, q2.py)."""

from q2 import seconds_to_time


def test_zero_is_midnight():
    # Boundary: midnight, all fields zero-padded.
    assert seconds_to_time(0) == "00:00:00"


def test_end_of_day():
    # Boundary: the last second of the day.
    assert seconds_to_time(86399) == "23:59:59"


def test_zero_padding():
    # Partition: fields below ten must be zero-padded.
    assert seconds_to_time(3671) == "01:01:11"


def test_sample_time():
    # Partition: a general mid-day time.
    assert seconds_to_time(43895) == "12:11:35"
