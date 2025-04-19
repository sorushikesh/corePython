"""
What is a Static Method?
- A method inside a class that doesn't use `self` or `cls`.
- It behaves like a regular function but is grouped logically inside a class.

How to define?
- Use the `@staticmethod` decorator above the method.

Why Use It?
- When the method doesn’t need access to instance or class state.
- For utility/helper functions related to the class.
"""

# Regular Class Example
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


def basic_static_method_demo():
    print("Static Method Demo")
    print("5 + 3 =", MathUtils.add(5, 3))
    print("Is 10 even?", MathUtils.is_even(10))
    print("-" * 40)


# Difference between instance vs static methods
class Message:
    def instance_greet(self, name):
        return f"Hello, {name}!"  # uses self (instance method)

    @staticmethod
    def static_greet(name):
        return f"Hi, {name}!"     # doesn't use self


def compare_methods_demo():
    print("Instance vs Static Method")
    m = Message()
    print("Instance:", m.instance_greet("Rushikesh"))
    print("Static:", Message.static_greet("Rushikesh"))
    print("-" * 40)


# ML Use Case: Preprocessing helper
class Preprocessor:
    @staticmethod
    def normalize(values):
        min_val = min(values)
        max_val = max(values)
        return [(x - min_val) / (max_val - min_val) for x in values]


def ml_static_method_demo():
    print("ML Use Case: Static method for normalization")
    data = [5, 10, 15, 20]
    print("Normalized:", Preprocessor.normalize(data))
    print("-" * 40)


# Backend Use Case: EmailValidator
class EmailValidator:
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email


def backend_static_method_demo():
    print("Backend Use Case: Email Validation")
    print("valid@example.com:", EmailValidator.is_valid("valid@example.com"))
    print("invalid-email:", EmailValidator.is_valid("invalid-email"))
    print("-" * 40)


def main():
    """
    Run all static method examples
    """
    basic_static_method_demo()
    compare_methods_demo()
    ml_static_method_demo()
    backend_static_method_demo()


if __name__ == "__main__":
    main()
