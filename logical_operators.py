"""
This script demonstrates all logical operators in Python with examples.
Logical operators:
1. and – True if both operands are true
2. or – True if at least one operand is true
3. not – True if the operand is false
"""

def logical_and_examples():
    """Demonstrates the 'and' logical operator."""
    print("🔹 AND Operator:")
    print(f"True and True = {True and True}")
    print(f"True and False = {True and False}")
    print(f"False and True = {False and True}")
    print(f"False and False = {False and False}")
    print("-" * 40)

def logical_or_examples():
    """Demonstrates the 'or' logical operator."""
    print("🔹 OR Operator:")
    print(f"True or True = {True or True}")
    print(f"True or False = {True or False}")
    print(f"False or True = {False or True}")
    print(f"False or False = {False or False}")
    print("-" * 40)

def logical_not_examples():
    """Demonstrates the 'not' logical operator."""
    print("🔹 NOT Operator:")
    print(f"not True = {not True}")
    print(f"not False = {not False}")
    print("-" * 40)

def main():
    """Main function to demonstrate all logical operators."""
    logical_and_examples()
    logical_or_examples()
    logical_not_examples()

if __name__ == "__main__":
    main()
