"""Tests for add_seconds_to_time (Lab 04, q2.py)."""

from q2 import add_seconds_to_time


def test_positive_delta_within_day():
    # Partition: no wrap-around needed.
    assert add_seconds_to_time("12:00:00", 0) == "12:00:00"
    assert add_seconds_to_time("10:00:00", 30) == "10:00:30"


def test_positive_delta_wraps_midnight():
    # Boundary: crossing midnight forward.
    assert add_seconds_to_time("23:59:50", 15) == "00:00:05"


def test_negative_delta_wraps_midnight():
    # Boundary: crossing midnight backward.
    assert add_seconds_to_time("00:00:10", -11) == "23:59:59"


def test_zero_delta():
    # Partition: the identity case.
    assert add_seconds_to_time("09:07:03", 0) == "09:07:03"


def test_positive_delta_spans_two_days():
    # Multi-day change: crosses midnight more than once.
    assert add_seconds_to_time("00:00:00", 172801) == "00:00:01"


def test_negative_delta_spans_two_days():
    # Multi-day change: crosses midnight backward more than once.
    assert add_seconds_to_time("00:00:00", -172801) == "23:59:59"
