from lib.report_length import *
import pytest

"""
tests the report length function returns correct string length for 1 - 9
"""
@pytest.mark.parametrize('test_input, expected', [('s', "This string was 1 characters long."),
                                                ('st', "This string was 2 characters long."),
                                                ('str', "This string was 3 characters long."),
                                                ('stri', "This string was 4 characters long."),
                                                ('strin', "This string was 5 characters long."),
                                                ('string', "This string was 6 characters long."),
                                                ('strings', "This string was 7 characters long."),
                                                ('stringst', "This string was 8 characters long."), 
                                                ('stringstr', "This string was 9 characters long.")])
def test_correct_string_length(test_input, expected):
    assert report_length(test_input) == expected

"""
tests the report length function fails if a none string is passed
as an argument
"""
def test_none_string():
    with pytest.raises(TypeError):
        report_length(55555)
    with pytest.raises(TypeError):
        report_length(True)

