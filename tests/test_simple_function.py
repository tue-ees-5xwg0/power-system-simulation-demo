from power_system_simulation.simple_function import add, multiply


def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4




def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a + b