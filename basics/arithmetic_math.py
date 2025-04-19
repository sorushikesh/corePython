"""
This script demonstrates all basic arithmetic operators and commonly used math functions in Python.
"""

import math

def arithmetic_operators(a, b):
    """Demonstrates basic arithmetic operations between two numbers."""
    print("Arithmetic Operators Demo")

    # Addition: Adds two numbers
    print(f"{a} + {b} = {a + b}  # Addition")

    # Subtraction: Subtracts second number from the first
    print(f"{a} - {b} = {a - b}  # Subtraction")

    # Multiplication: Multiplies two numbers
    print(f"{a} * {b} = {a * b}  # Multiplication")

    # Division: Divides first number by the second (returns float)
    print(f"{a} / {b} = {a / b}  # Division")

    # Floor Division: Divides and rounds down to nearest integer
    print(f"{a} // {b} = {a // b}  # Floor Division")

    # Modulus: Returns the remainder
    print(f"{a} % {b} = {a % b}  # Modulus (Remainder)")

    # Exponentiation: Raises a to the power of b
    print(f"{a} ** {b} = {a ** b}  # Exponentiation")

    print("-" * 50)

def math_functions_demo(x):
    """Demonstrates math module functions with one input number."""
    print("Math Module Functions Demo")

    # Returns the smallest integer greater than or equal to x
    print(f"math.ceil({x}) = {math.ceil(x)}  # Ceiling value")

    # Returns the largest integer less than or equal to x
    print(f"math.floor({x}) = {math.floor(x)}  # Floor value")

    # Returns the square root of x
    print(f"math.sqrt({x}) = {math.sqrt(x)}  # Square root")

    # Raises x to the power of 2
    print(f"math.pow({x}, 2) = {math.pow(x, 2)}  # x raised to power 2")

    # Returns the absolute (non-negative) value of x
    print(f"math.fabs({x}) = {math.fabs(x)}  # Absolute value")

    # Returns natural logarithm (base e) of x
    print(f"math.log({x}) = {math.log(x)}  # Natural log (ln)")

    # Returns base-10 logarithm of x
    print(f"math.log10({x}) = {math.log10(x)}  # Base-10 log")

    # Returns e raised to the power of x
    print(f"math.exp({x}) = {math.exp(x)}  # Exponential of x (e^x)")

    # Returns factorial of a number (e.g., 5! = 120)
    print(f"math.factorial(5) = {math.factorial(5)}  # Factorial of 5")

    # Returns the constant Pi (π ≈ 3.14159)
    print(f"math.pi = {math.pi}  # Pi constant")

    # Returns Euler's number (e ≈ 2.71828)
    print(f"math.e = {math.e}  # Euler’s number")

    print("-" * 50)

def main():
    """Main function to call all demos."""
    a = 15
    b = 4
    x = 7.3

    arithmetic_operators(a, b)
    math_functions_demo(x)

if __name__ == "__main__":
    main()
