"""
What is a Module?
- A Python file (`.py`) that contains functions, classes, or variables.
- Modules help break code into logical, reusable, and manageable parts.

Why Use Modules?
- Code reusability & separation of concerns.
- Helps in large-scale applications and team collaboration.
- Useful for creating utility functions, ML pipelines, database handlers, etc.

Types of Modules:
1. Built-in Modules → `math`, `os`, `random`, `datetime`, etc.
2. Custom Modules  → Your own `.py` files
3. External Modules → Installed via pip (e.g., `numpy`, `pandas`, `requests`)
"""

# Built-in Module: math
import math

def using_builtin_module():
    print("Using math module:")
    print("Square root of 16:", math.sqrt(16))
    print("Pi constant:", math.pi)
    print("-" * 40)


# Import specific items
from datetime import datetime, timedelta

def using_selective_import():
    print("Using datetime module:")
    print("Current time:", datetime.now())
    print("Tomorrow:", datetime.now() + timedelta(days=1))
    print("-" * 40)


# Aliased import
import random as rnd

def using_aliased_module():
    print("Using alias for random module:")
    print("Random number:", rnd.randint(1, 10))
    print("-" * 40)


# Custom Module Example
# Assume we have a file named `math_utils.py`:
# def add(a, b): return a + b
# def multiply(a, b): return a * b
# import math_utils
# print(math_utils.add(2, 3))

def custom_module_usage_note():
    print("Custom Module (concept):")
    print("Create file: math_utils.py with functions")
    print("Then: import math_utils and use its methods")
    print("-" * 40)


# External Module Example (Numpy)
# Run: pip install numpy
try:
    import numpy as np

    def using_external_module():
        print("Using external module (numpy):")
        arr = np.array([1, 2, 3])
        print("Numpy array:", arr)
        print("Mean:", np.mean(arr))
        print("-" * 40)
except ImportError:
    def using_external_module():
        print("numpy not installed. Run: pip install numpy")
        print("-" * 40)


def main():
    """
    Run all module examples.
    """
    using_builtin_module()
    using_selective_import()
    using_aliased_module()
    custom_module_usage_note()
    using_external_module()


if __name__ == "__main__":
    main()
