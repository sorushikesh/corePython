"""
What is Encapsulation?
- The concept of **hiding internal object details** and exposing only what's necessary.
- Achieved in Python using:
    1. **Private attributes/methods** with `_` or `__`
    2. **Getter/Setter** methods or `@property`
- Keeps objects **self-contained**, **secure**, and **modular**.

Why Use It?
- Prevent accidental access/modification of internal data.
- Enforce data validation and access control.
- Makes your code easier to maintain.
"""

# Basic Encapsulation Using Private Variables
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self.__balance = balance  # private (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"Withdrew ₹{amount}"

    def get_balance(self):
        return self.__balance


def basic_encapsulation_demo():
    print("Basic Encapsulation")
    acc = BankAccount("Rushikesh", 1000)

    print("Owner:", acc.owner)
    print("Balance (via method):", acc.get_balance())

    acc.deposit(500)
    print("Balance after deposit:", acc.get_balance())

    print(acc.withdraw(2000))  # will fail
    print(acc.withdraw(1000))  # will succeed
    print("Final Balance:", acc.get_balance())

    try:
        print(acc.__balance)  # AttributeError (name mangled)
    except AttributeError as e:
        print("Access Error:", e)

    print("-" * 40)


# Encapsulation using @property
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


def property_encapsulation_demo():
    print("Encapsulation with @property")
    temp = Temperature(25)
    print("Fahrenheit:", temp.fahrenheit)

    temp.fahrenheit = 98.6
    print("Updated Celsius:", temp._celsius)
    print("Re-calculated Fahrenheit:", temp.fahrenheit)
    print("-" * 40)


# Real-World ML Use Case
class Model:
    def __init__(self, name, learning_rate):
        self.name = name
        self.__learning_rate = learning_rate

    def train(self):
        return f"Training {self.name} with LR={self.__learning_rate}"

    def update_learning_rate(self, lr):
        if 0 < lr < 1:
            self.__learning_rate = lr
        else:
            raise ValueError("Invalid learning rate!")


def ml_encapsulation_demo():
    print("ML Use Case: Encapsulation in Model")
    model = Model("CNN", 0.01)
    print(model.train())

    model.update_learning_rate(0.001)
    print("Updated:", model.train())

    try:
        model.__learning_rate = 100  # Will not update the actual value
        print("Bad update:", model.train())
    except Exception as e:
        print("Error:", e)

    print("-" * 40)


def main():
    """
    Run all encapsulation examples
    """
    basic_encapsulation_demo()
    property_encapsulation_demo()
    ml_encapsulation_demo()


if __name__ == "__main__":
    main()
