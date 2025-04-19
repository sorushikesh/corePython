"""
What is Exception Handling?
- A way to handle runtime errors gracefully.
- Prevents app crashes by using `try-except-finally`.

Why Use It?
- Clean error reporting
- Application stability
- Debugging/logging real issues
"""

# Basic try-except
def basic_handling():
    print("Basic Exception Handling")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print("-" * 40)


# Catch multiple exception types
def multiple_exception_handling():
    print("Multiple Exception Types")
    try:
        x = int("abc")
        y = 10 / 0
    except ValueError as ve:
        print("ValueError:", ve)
    except ZeroDivisionError as zde:
        print("ZeroDivisionError:", zde)
    print("-" * 40)


# try-except-else-finally
def full_structure_handling():
    print("try-except-else-finally")

    try:
        x = 5
        print("Calculation:", x * 2)
    except Exception as e:
        print("Something went wrong:", e)
    else:
        print("No exceptions occurred")
    finally:
        print("🔚 Always executes (cleanup/log)")
    print("-" * 40)


# Raising exceptions manually
def raising_exceptions():
    print("Raising Exceptions")
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("-" * 40)


# Custom Exception Class
class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: Available ₹{balance}, Tried ₹{amount}")


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def spend(self, amount):
        if amount > self.balance:
            raise InsufficientFunds(self.balance, amount)
        self.balance -= amount
        return f"💸 Spent ₹{amount}, Remaining: ₹{self.balance}"


def custom_exception_demo():
    print("Custom Exception Example")

    wallet = Wallet(1000)

    try:
        print(wallet.spend(300))
        print(wallet.spend(800))  # This will raise custom exception
    except InsufficientFunds as e:
        print("⚠️ Error:", e)
    print("-" * 40)


# ML Use Case: Validate training data
def ml_exception_use_case():
    print("ML Use Case: Data Validation")

    def train_model(data):
        if not data:
            raise ValueError("Training data cannot be empty")
        print("Model trained on", len(data), "samples")

    try:
        train_model([])
    except ValueError as e:
        print("ML Error:", e)
    print("-" * 40)


def main():
    """
    Run all exception handling examples
    """
    basic_handling()
    multiple_exception_handling()
    full_structure_handling()

    try:
        raising_exceptions()
    except ValueError as e:
        print("Manually raised error caught:", e)

    custom_exception_demo()
    ml_exception_use_case()


if __name__ == "__main__":
    main()
