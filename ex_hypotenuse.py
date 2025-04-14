"""
This script calculates the hypotenuse of a right-angled triangle
based on the two other side lengths provided by the user.
"""

import math

def hypotenuse(size1, size2):
    """
    Calculate the hypotenuse of a right-angled triangle.

    Args:
        size1 (float): One side of the triangle.
        size2 (float): Another side of the triangle.

    Returns:
        float: Length of the hypotenuse.
    """
    print(f"Triangle side lengths: {size1} and {size2}")

    # Using Pythagoras theorem: c² = a² + b²
    hypo = math.sqrt(size1 ** 2 + size2 ** 2)

    print(
        f"Hypotenuse of triangle with sizes {size1} and {size2} is {hypo:.2f}"
    )
    return hypo

def main():
    """
    Main function to run the hypotenuse calculation.
    """
    size1 = float(input("Enter the first side of the triangle: "))
    size2 = float(input("Enter the second side of the triangle: "))
    hypotenuse(size1, size2)

if __name__ == "__main__":
    main()
