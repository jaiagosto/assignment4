# tests/test_operations.py

"""
Unit tests for the operations module using pytest.

This test suite covers both positive and negative scenarios for the Operation
class's static methods. It ensures that arithmetic operations perform correctly
and handle edge cases appropriately.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from app.operations import Operation


# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

def test_addition_positive():
    """
    Test the addition method with two positive numbers.
    
    This test verifies that adding two positive numbers returns the correct sum.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 15.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_negative_numbers():
    """
    Test the addition method with two negative numbers.
    
    This test verifies that adding two negative numbers returns the correct sum.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -15.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_positive_negative():
    """
    Test the addition method with one positive and one negative number.
    
    This test verifies that adding a positive and a negative number returns the correct sum.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 5.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + ({b}) to be {expected_result}, got {result}"


def test_addition_with_zero():
    """
    Test the addition method with zero as one of the operands.
    
    This test verifies that adding zero to a number returns the number itself.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

def test_subtraction_positive():
    """
    Test the subtraction method with two positive numbers.
    
    This test verifies that subtracting two positive numbers returns the correct difference.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 5.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


def test_subtraction_negative_numbers():
    """
    Test the subtraction method with two negative numbers.
    
    This test verifies that subtracting two negative numbers returns the correct difference.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -5.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_positive_negative():
    """
    Test the subtraction method with one positive and one negative number.
    
    This test verifies that subtracting a negative number from a positive number returns the correct difference.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 15.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_with_zero():
    """
    Test the subtraction method with zero as one of the operands.
    
    This test verifies that subtracting zero from a number returns the number itself.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

def test_multiplication_positive():
    """
    Test the multiplication method with two positive numbers.
    
    This test verifies that multiplying two positive numbers returns the correct product.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_negative_numbers():
    """
    Test the multiplication method with two negative numbers.
    
    This test verifies that multiplying two negative numbers returns the correct product.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_positive_negative():
    """
    Test the multiplication method with one positive and one negative number.
    
    This test verifies that multiplying a positive number by a negative number returns the correct product.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * ({b}) to be {expected_result}, got {result}"


def test_multiplication_with_zero():
    """
    Test the multiplication method with zero as one of the operands.
    
    This test verifies that multiplying any number by zero returns zero.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 0.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

def test_division_positive():
    """
    Test the division method with two positive numbers.
    
    This test verifies that dividing two positive numbers returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_negative_numbers():
    """
    Test the division method with two negative numbers.
    
    This test verifies that dividing two negative numbers returns the correct quotient.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_positive_negative():
    """
    Test the division method with one positive and one negative number.
    
    This test verifies that dividing a positive number by a negative number returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / ({b}) to be {expected_result}, got {result}"


def test_division_with_zero_divisor():
    """
    Test the division method with zero as the divisor.
    
    This test verifies that dividing any number by zero raises a ValueError.
    """
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operation.division(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero is not allowed."


def test_division_with_zero_numerator():
    """
    Test the division method with zero as the numerator.
    
    This test verifies that dividing zero by a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Power Method
# -----------------------------------------------------------------------------------

def test_power_positive_base_positive_exponent():
    """
    Test the power method with positive base and positive exponent.
    
    This test verifies that raising a positive number to a positive power returns the correct result.
    """
    # Arrange
    base = 2.0
    exponent = 3.0
    expected_result = 8.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_positive_base_negative_exponent():
    """
    Test the power method with positive base and negative exponent.
    
    This test verifies that raising a positive number to a negative power returns the correct result.
    """
    # Arrange
    base = 2.0
    exponent = -3.0
    expected_result = 0.125

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_negative_base_positive_exponent():
    """
    Test the power method with negative base and positive exponent.
    
    This test verifies that raising a negative number to a positive power returns the correct result.
    """
    # Arrange
    base = -2.0
    exponent = 3.0
    expected_result = -8.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_negative_base_even_exponent():
    """
    Test the power method with negative base and even exponent.
    
    This test verifies that raising a negative number to an even power returns a positive result.
    """
    # Arrange
    base = -2.0
    exponent = 4.0
    expected_result = 16.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_base_to_zero():
    """
    Test the power method with exponent of zero.
    
    This test verifies that any non-zero number raised to the power of zero returns 1.
    """
    # Arrange
    base = 5.0
    exponent = 0.0
    expected_result = 1.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_zero_base_positive_exponent():
    """
    Test the power method with zero base and positive exponent.
    
    This test verifies that zero raised to any positive power returns zero.
    """
    # Arrange
    base = 0.0
    exponent = 5.0
    expected_result = 0.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_zero_base_zero_exponent():
    """
    Test the power method with zero base and zero exponent.
    
    This test verifies that 0^0 raises a ValueError as it's mathematically undefined.
    """
    # Arrange
    base = 0.0
    exponent = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operation.power(base, exponent)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "0^0 is undefined."


def test_power_base_one():
    """
    Test the power method with base of one.
    
    This test verifies that one raised to any power returns one.
    """
    # Arrange
    base = 1.0
    exponent = 100.0
    expected_result = 1.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_fractional_exponent():
    """
    Test the power method with fractional exponent (square root).
    
    This test verifies that raising a number to a fractional power works correctly.
    """
    # Arrange
    base = 4.0
    exponent = 0.5
    expected_result = 2.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"

# -----------------------------------------------------------------------------------
# Test Modulus Method
# -----------------------------------------------------------------------------------

def test_modulus_positive_numbers():
    """
    Test the modulus method with two positive numbers.
    
    This test verifies that the modulus of two positive numbers returns the correct remainder.
    """
    # Arrange
    a = 10.0
    b = 3.0
    expected_result = 1.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_negative_dividend():
    """
    Test the modulus method with negative dividend.
    
    This test verifies that modulus works correctly with negative dividend.
    """
    # Arrange
    a = -10.0
    b = 3.0
    expected_result = 2.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_negative_divisor():
    """
    Test the modulus method with negative divisor.
    
    This test verifies that modulus works correctly with negative divisor.
    """
    # Arrange
    a = 10.0
    b = -3.0
    expected_result = -2.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_both_negative():
    """
    Test the modulus method with both negative numbers.
    
    This test verifies that modulus works correctly when both numbers are negative.
    """
    # Arrange
    a = -10.0
    b = -3.0
    expected_result = -1.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_zero_dividend():
    """
    Test the modulus method with zero as dividend.
    
    This test verifies that 0 mod any number returns 0.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_zero_divisor():
    """
    Test the modulus method with zero as divisor.
    
    This test verifies that modulus by zero raises a ValueError.
    """
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operation.modulus(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Modulus by zero is not allowed."


def test_modulus_evenly_divisible():
    """
    Test the modulus method when dividend is evenly divisible by divisor.
    
    This test verifies that modulus returns 0 when there's no remainder.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_fractional_result():
    """
    Test the modulus method with fractional numbers.
    
    This test verifies that modulus works with floating-point numbers.
    """
    # Arrange
    a = 7.5
    b = 2.0
    expected_result = 1.5

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.addition, '10', 5.0, TypeError),
    (Operation.subtraction, 10.0, '5', TypeError),
    (Operation.multiplication, '10', '5', TypeError),
    (Operation.division, 10.0, '5', TypeError),
    (Operation.power, '2', 3.0, TypeError),
    (Operation.power, 2.0, '3', TypeError),
    (Operation.modulus, '10', 3.0, TypeError),
    (Operation.modulus, 10.0, '3', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """
    Test that arithmetic methods raise TypeError when provided with invalid input types.
    
    This test verifies that providing non-float inputs to the arithmetic methods raises
    a TypeError, as the operations are intended for floating-point numbers.
    """
    # Arrange
    # No setup needed as the invalid inputs are provided directly

    # Act & Assert
    with pytest.raises(expected_exception):
        calc_method(a, b)