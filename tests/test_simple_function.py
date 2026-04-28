from pytest import raises

from power_system_simulation.simple_function import add, divide, multiply


def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4

def test_divide():
    assert divide(4, 2) == 2

def test_divide_by_zero():
    with raises(ValueError, match="Cannot divide by zero"):
        divide(4, 0)
