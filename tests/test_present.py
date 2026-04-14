from lib.present import *
import pytest

def test_no_contents_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(1)
    with pytest.raises(Exception)as e:
        present.wrap(1)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."