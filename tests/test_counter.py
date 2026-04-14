from lib.counter import Counter
import pytest
"""
test counts to first number given 
"""
def test_counts_to_five():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
"""
test counts first number given for all single digits 1 - 9
"""
@pytest.mark.parametrize('test_input, expected', [(1, 1), (2, 2), (3, 3),
                                                (4, 4), (5, 5), (6, 6), 
                                                (7, 7), (8, 8), (9, 9), ])
def test_counts_one_to_nine(test_input, expected):
    counter = Counter()
    counter.add(test_input)
    assert counter.report() == f"Counted to {expected} so far."

"""
test successfully adds second number to existing count
"""
def test_adds_second_number():
    counter = Counter()
    counter.add(5)
    counter.add(6)
    assert counter.report() == "Counted to 11 so far."
"""
test succesfully adds second number for all single digit numbers 1 - 9
"""
@pytest.mark.parametrize('first_input, second_input, expected', [(1, 1, 2), (2, 2, 4), (3, 3, 6),
                                                (4, 4, 8), (5, 5, 10), (6, 6, 12), 
                                                (7, 7, 14), (8, 8, 16), (9, 9, 18), ])
def test_adds_second_number_one_to_nine(first_input, second_input, expected):
    counter = Counter()
    counter.add(first_input)
    counter.add(second_input)
    assert counter.report() == f"Counted to {expected} so far."
