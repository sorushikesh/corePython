"""
This script calculates the circumference of a circle based on the given radius.
"""

import math

def circumference(radius):
    """
    Calculate the circumference of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Circumference of the circle.
    """
    print(f"Radius of circle: {radius}")
    circ = 2 * math.pi * radius
    print(f"Circumference of circle with radius {radius} is {circ:.2f}") # :.2f round the value upto 2 digits
    return circ

def main():
    """
    Main function to run the circumference calculation.
    """
    radius = float(input("Enter the radius of the circle: "))
    circumference(radius)

if __name__ == "__main__":
    main()
