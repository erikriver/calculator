from app import calculator


def test_add():
    assert calculator("2+2.0") == 4.0
    assert calculator(".2 + 2.0") == 2.2


def test_subtract():
    assert calculator(" 2-2") == 0
    assert round(calculator(".1-.4"), 2) == -0.3


def test_multiply():
    assert calculator("2* 2") == 4
    assert round(calculator("0.2 * 0.2"), 3) == 0.04


def test_divide():
    assert calculator("2/2") == 1


def test_multilple_operations():
    assert calculator("-.2+0.2") == 0
    assert calculator("12-2+4/3*6") == 18.0

def test_zero_division():
    assert calculator("2/0") == "E: Zero Division"
