"""
What is `super()`?
- A built-in function used to **call a method from the parent class**.
- Primarily used in **inheritance** to reuse and extend behavior of the base class.

Why Use `super()`?
- Avoid code duplication.
- Ensure proper method resolution in multi-level/multiple inheritance.
- Recommended over direct parent class calls (e.g., `Parent.method(self)`).

Common Use:
1. Inside `__init__()` to initialize base class.
2. Inside methods to extend or reuse base logic.
"""

# Parent class
class User:
    def __init__(self, name):
        self.name = name
        print(f"[User] Created user: {self.name}")

    def describe(self):
        return f"User: {self.name}"


# Child class using super()
class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)  # Call parent constructor
        self.level = level
        print(f"[Admin] Access level set to: {self.level}")

    def describe(self):
        base = super().describe()  # Reuse parent's method
        return f"{base} | Role: Admin, Level: {self.level}"


def basic_super_demo():
    print("Basic super() Demo")
    admin = Admin("Rushikesh", "Full")
    print(admin.describe())
    print("-" * 40)


# Multi-level inheritance example
class A:
    def __init__(self):
        print("Init A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init B")

class C(B):
    def __init__(self):
        super().__init__()
        print("Init C")


def multilevel_super_demo():
    print("Multi-level super() Demo")
    c = C()  # Will call A → B → C in order
    print("-" * 40)


# Real-world ML example: BaseModel → CNNModel
class BaseModel:
    def __init__(self, name):
        self.name = name

    def summary(self):
        return f"Base model: {self.name}"


class CNNModel(BaseModel):
    def __init__(self, name, layers):
        super().__init__(name)  # Initialize BaseModel
        self.layers = layers

    def summary(self):
        base = super().summary()
        return f"{base} | Type: CNN | Layers: {self.layers}"


def ml_super_demo():
    print("ML Use Case: super() in model inheritance")
    cnn = CNNModel("ImageClassifier", 10)
    print(cnn.summary())
    print("-" * 40)


def main():
    """
    Run all super() usage examples
    """
    basic_super_demo()
    multilevel_super_demo()
    ml_super_demo()


if __name__ == "__main__":
    main()
