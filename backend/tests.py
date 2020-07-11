from app import calculator


def test_add():
    assert calculator(2, 2, '+') == 4

def test_subtract():
    assert calculator(2, 2, '-') == 0

def test_multiply():
    assert calculator(2, 2, '*') == 4

def test_divide():
    assert calculator(2, 2, '/') == 1