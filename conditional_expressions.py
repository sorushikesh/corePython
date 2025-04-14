"""
This script demonstrates conditional expressions (ternary operator) in Python.
It shows how to use single-line if-else logic with practical examples.
"""


def age_check(age):
    """Determine if a person is an adult or minor."""
    result = "Adult" if age >= 18 else "Minor"
    print(f"Age {age} → {result}")


def even_or_odd(number):
    """Check if a number is even or odd using a conditional expression."""
    result = "Even" if number % 2 == 0 else "Odd"
    print(f"{number} is {result}")


def maximum_of_two(a, b):
    """Find the maximum of two numbers."""
    max_val = a if a > b else b
    print(f"Max of {a} and {b} is {max_val}")


def sign_check(num):
    """Check if a number is positive, negative, or zero using nested conditional expressions."""
    result = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
    print(f"{num} is {result}")


def main():
    """Main function to demonstrate conditional expressions."""
    age_check(21)
    age_check(16)

    even_or_odd(10)
    even_or_odd(7)

    maximum_of_two(5, 9)
    maximum_of_two(12, 3)

    sign_check(10)
    sign_check(0)
    sign_check(-5)


if __name__ == "__main__":
    main()
