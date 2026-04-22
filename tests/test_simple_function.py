from power_system_simulation.simple_function import add, multiply, divide
import pytest

def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4

def test_divide():
    assert divide(2,2) == 1

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(2, 0)