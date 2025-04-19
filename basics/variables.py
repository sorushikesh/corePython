"""This module demonstrates basic Python variables and typecasting."""

# Variables:
# Variables in Python are references to objects in memory.
# When we assign a value to a variable, we bind that name to an object in memory.

# String
FIRST_NAME = "Rushikesh"
print(FIRST_NAME)
print(f"Hello {FIRST_NAME}")

# Integer
AGE = 26
print(f"Hi I'm {FIRST_NAME} and I'm {AGE} years old")

# Float
PRICE = 10.99
print(f"The price is ${PRICE}")

# Boolean
IS_PASSED = True
print(f"Passed: {IS_PASSED}")

# Typecasting
# Type Casting is the process of converting the value of one data type into another.
# Python provides built-in functions like int(), float(), str() to ease type casting.

print(f"Variable {FIRST_NAME} is of type {type(FIRST_NAME)}")

# Convert float to int, then back to float and string
VAL1 = 11.2
print(f"Variable {VAL1} is of type {type(VAL1)}")

VAL1 = int(VAL1)
print(f"Variable {VAL1} is of type {type(VAL1)} after conversion to int")

VAL1 = float(VAL1)
print(f"Variable {VAL1} is of type {type(VAL1)} after conversion to float")

VAL1 = str(VAL1)
print(f"Variable {VAL1} is of type {type(VAL1)} after conversion to string")
