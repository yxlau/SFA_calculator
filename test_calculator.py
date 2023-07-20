import pytest
from calculator import *

# handles addition
def test_addition():
  assert add(2, 3) == 5

# handles subtraction
def test_subtraction():
  assert subtract(10, 1) == 9

# handles multiplication
def test_multiply():
  assert multiply(1, 10) == 10

# handles division
# DONE: handles zero division 
def test_divide():
  assert divide(1, 0) == "Cannot divide by 0"
  assert divide(10, 3) == 10/3
  assert divide(99,2) == 49.5

def test_get_num(monkeypatch):
  # Mock user input for valid integer
  monkeypatch.setattr('builtins.input', lambda _: "42")
  assert get_num("Enter a number: ") == 42

  # Mock user input for invalid input (non-integer)
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  assert get_num(
      "Enter a number: ") == "Please enter a valid integer"

def test_get_selection(monkeypatch):
    # Mock user input for valid selection
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert get_selection() == 3

    # Mock user input for invalid selection
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(ValueError):
        get_selection()

