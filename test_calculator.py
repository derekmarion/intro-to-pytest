import calculator
import pytest

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_subtract():
    assert calculator.calculate(10, 5, "subtract") == 5

def test_multiply():
    assert calculator.calculate(10, 5, "multiply") == 50

def test_divide():
    assert calculator.calculate(10, 5, "divide") == 2

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20.0"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios

def test_addNegative():
    assert calculator.calculate(10, -4, "add") == 6

def test_divideByZero():
    with pytest.raises(ValueError) as e:
        calculator.calculate(10, 0, "divide")
    assert str(e.value) == "Cannot divide by zero"