# Lab 4 Report

Name:

Set:

Complete the short prompts below and submit this file with `q1.py`, `q2.py`,
and your corrected `digit_streak.py` on Learning Hub. No screenshots are required.

## Debugging Record

Before running the tests, predict the value the original buggy code returns for
`longest_digit_streak("A123")`. Keep your original prediction.

- Predicted result: 3

After running the original tests, record these before repairing the code:

- Failed test name: test_streak_at_end
- Expected result: 3
- Actual result: 2

Statement changed (original and replacement):
Original:
    while index < len(text)-1:
Replacement:
    while index < len(text):
Explain the cause and repair together in two or three sentences:
The bug was caused by the -1 in this statement, because if the list number was part of the 
longest_streak it would not be counted because the statement is < andn we took one away from the length
to give us the indices. We fixed the bug by removing the -1 so that the loop will acutally reach the last index.
Final pytest summary after rerunning `test_digit_streak.py` (copy the summary text):
============================= test session starts ==============================
collecting ... collected 3 items

test_digit_streak.py::test_empty_text PASSED                             [ 33%]
test_digit_streak.py::test_internal_streak PASSED                        [ 66%]
test_digit_streak.py::test_streak_at_end PASSED                          [100%]

============================== 3 passed in 0.01s ===============================