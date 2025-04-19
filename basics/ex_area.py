"""
This script calculates the area of a circle based on the given radius.
"""

import math

def area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: area of the circle.
    """
    print(f"Radius of circle: {radius}")
    circ = math.pi * math.pow(radius, 2)
    print(f"area of circle with radius {radius} is {circ:.2f}")
    # :.2f round the value upto 2 digits
    return circ

def main():
    """
    Main function to run the area calculation.
    """
    radius = float(input("Enter the radius of the circle: "))
    area(radius)

if __name__ == "__main__":
    main()
