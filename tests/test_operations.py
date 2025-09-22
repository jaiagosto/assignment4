"""
tests/test_operations.py

Module 3 tests the Operations class which does basic math such as add, subtract, multiply, and divide. 
We will use pytest to run the same test with different inputs, instead of writing multiple tests for every number.

Parametized tests helps by saving us from duplicating codes
while making sure our tests are covered woth less inputs. 
"""

import pytest # Importing the pytest library to use its features for testing
from typing import Union # Importing Union from typing to specify multiple possible types for function parameters
from app.operations import Operations # Importing the Operations class from the app.operations module

# Creating a label/shortcut for numbers that can be either int (whole numbers) or float (decimal numbers)
Number = Union[int, float]

#-----------------------------------------------------
# Unit Tests for the 'addition' method
#-----------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),          # Test adding two positive integers
        (0, 0, 0),          # Test adding two zeros
        (-1, 1, 0),        # Test adding a negative and a positive integer
        (2.5, 3.5, 6.0),    # Test adding two positive floats
        (-2.5, 3.5, 1.0),   # Test adding a negative and a positive float
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    """
    Test the addition method of the Operations class with various inputs.
    
    This parameterized test checks the addition of different combinations 
    of integers and floats with positive and negative numbers.

    Parameters:
    - a (Number): The first number to add (int or float).
    - b (Number): The second number to add (int or float).
    - expected (Number): The expected result of the addition (int or float).

    Steps:
    1. Call the 'addition' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_addition(2, 3, 5)
    >>> test_addition(-1, 1, 0)
    """
    #Create an example of the Operations class

    #Call the 'addition' method with the provided arguments
    result = Operations.addition(a, b)

    #Assert that the result of addition(a,b) matches the expected value
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}" 

# ----------------------------------------
# Unit Tests for the 'subtraction' Method
# ----------------------------------------

@pytest.mark.parametrize(
  "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (0, 0, 0),           # Test subtracting two zeros
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (10.5, 5.5, 5.0),    # Test subtracting two positive floats
        (-10.5, -5.5, -5.0), # Test subtracting two negative floats
    ],
    ids=[
        "subtract_smaller_positive_integer_from_larger",
         "subtract_two_zeros",
         "subtract_negative_integer_from_negative_integer",
         "subtract_two_positive_floats",
         "subtract_two_negative_floats",
        ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """
    Test the subtraction method of the Operations class with various inputs.
    
    This parameterized test checks the subtraction of different combinations 
    of integers and floats with positive and negative numbers.

    Parameters:
    - a (Number): The first number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction (int or float).

    Steps:
    1. Call the 'subtraction' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtraction(5, 3, 2)
    >>> test_subtraction(-5, -3, -2)
    """
    # Create an example of the Operations class

    # Call the 'subtraction' method with the provided arguments
    result = Operations().subtraction(a, b)

    # Assert that the result of subtraction(a,b) matches the expected value
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"

# ------------------------------------------------
# Unit Tests for the 'multiplication' Method
# ------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),            # Test multiplying two positive integers
        (0, 10, 0),           # Test multiplying zero with a positive integer
        (-2, 3, -6),          # Test multiplying two negative integers
        (2.5, 4.0, 10.0),     # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),   # Test multiplying a negative float with a positive float
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_zero_with_positive_integer",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float",
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """
    Test the multiplication method of the Operations class with various inputs.
    
    This parameterized test checks the multiplication of different combinations 
    of integers and floats with positive and negative numbers.

    Parameters:
    - a (Number): The first number to multiply (int or float).
    - b (Number): The second number to multiply (int or float).
    - expected (Number): The expected result of the multiplication (int or float).

    Steps:
    1. Call the 'multiplication' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiplication(2, 3, 6)
    >>> test_multiplication(-2, 3, -6)
    """
    # Create an example of the Operations class

    # Call the 'multiplication' method with the provided arguments
    result = Operations().multiplication(a, b)

    # Assert that the result of multiplication(a,b) matches the expected value
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

# --------------------------------------------
# Unit Tests for the 'division' Method
# --------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),          # Test dividing two positive integers
        (-6, -3, 2.0),        # Test dividing two negative integers
        (6.0, 3.0, 2.0),      # Test dividing two positive integers
        (-6.0, 3.0, -2.0),    # Test dividing a negative float by a positive float
        (0, 5, 0.0),          # Test dividing zero by a positive integer

    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    """
    Test the division method of the Operations class with various inputs.
    
    This parameterized test checks the division of different combinations 
    of integers and floats with positive and negative numbers.

    Parameters:
    - a (Number): The numerator (int or float).
    - b (Number): The denominator (int or float).
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'division' method with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_division(6, 3, 2.0)
    >>> test_division(-6, -3, 2.0)
    """
    # Create an example of the Operations class

    # Call the 'division' method with the provided arguments
    result = Operations().division(a, b)

    # Assert that the result of division(a,b) matches the expected value
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"

# ------------------------------------------------
# Negative Test Case: Division by Zero
# ------------------------------------------------

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),        # Test dividing a positive dividend by zero
        (-1, 0),       # Test dividing a negative dividend by zero
        (0, 0),        # Test dividing zero by zero
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    """
    Test the division method of the Operations class for division by zero.
    
    This parameterized test checks that dividing any number by zero raises a ValueError.

    Parameters:
    - a (Number): The numerator (int or float).
    - b (Number): The denominator (int or float), which is zero in these tests.

    Steps:
    1. Call the 'division' method with arguments 'a' and 'b'.
    2. Assert that a ValueError is raised with the message "Division by zero is not allowed."

    Example:
    >>> test_division_by_zero(1, 0)
    >>> test_division_by_zero(-1, 0)
    """
    # Create an example of the Operations class

    # Use pytest.raises to check that a ValueError is raised when dividing by zero
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        # Attempt to divide 'a' by 'b', which should raise a ValueError
        Operations.division(a, b)

    # Assert that the exception message contains the expected error message
    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '[excinfo.value]'"
    