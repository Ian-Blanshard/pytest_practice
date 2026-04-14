from lib.greet import *

def test_greet_returns_hello_ian_for_ian():
    result = greet('ian')
    assert result == 'Hello, ian!'