from lib.gratitudes import *

"""
test instances with no gratitudes return correct string
"""
def test_init_returns_correct_string():
    person = Gratitudes()
    assert person.format() == "Be grateful for: "
"""
test single gratitude is returned correctly
"""
def test_single_gratitude():
    person = Gratitudes()
    person.add('dog')
    assert person.format() == "Be grateful for: dog"
"""
test multiple gratitudes are returned correctly
"""
def test_multiple_gratitudes():
    person = Gratitudes()
    person.add('dog')
    person.add('cat')
    assert person.format() == "Be grateful for: dog, cat"