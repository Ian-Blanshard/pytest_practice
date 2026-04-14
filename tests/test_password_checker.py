from lib.password_checker import *
import pytest

def test_password_greater_than_seven():
    password = PasswordChecker()
    assert password.check('password123') == True

def test_invalid_password_raises_exception():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('passwor')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."clear