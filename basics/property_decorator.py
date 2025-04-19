"""
What is @property?
- A built-in decorator that allows a method to be accessed like an attribute.
- Used to get, set, or delete attributes with added control/logic.
- Helps enforce encapsulation.

Why Use It?
- Hide internal variables.
- Add validation on setting attributes.
- Simpler, cleaner syntax: `obj.value` instead of `obj.get_value()`
"""

# Example: Encapsulating `balance` with @property
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # private by convention

    @property
    def balance(self):
        print("[INFO] Getting balance...")
        return self._balance

    @balance.setter
    def balance(self, value):
        print("[INFO] Setting balance...")
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    @balance.deleter
    def balance(self):
        print("[INFO] Deleting balance...")
        del self._balance


def property_basic_demo():
    print("Basic Property Demo")
    acc = BankAccount("Rushikesh", 1000)

    print("Balance:", acc.balance)  # calls getter

    acc.balance = 1500              # calls setter
    print("Updated Balance:", acc.balance)

    try:
        acc.balance = -500          # validation triggers error
    except ValueError as e:
        print("Error:", e)

    del acc.balance                 # calls deleter
    print("-" * 40)


# ML Example: Auto-normalize value using @property
class Feature:
    def __init__(self, value):
        self._raw = value

    @property
    def normalized(self):
        # Normalize between 0 and 1
        return self._raw / 100.0

    @normalized.setter
    def normalized(self, val):
        self._raw = val * 100


def ml_property_demo():
    print("ML Use Case: Normalized Feature")
    f = Feature(45)
    print("Normalized:", f.normalized)  # 0.45

    f.normalized = 0.9  # sets raw to 90
    print("Updated raw:", f._raw)
    print("Re-Normalized:", f.normalized)
    print("-" * 40)


def main():
    """
    Run all @property examples
    """
    property_basic_demo()
    ml_property_demo()


if __name__ == "__main__":
    main()
