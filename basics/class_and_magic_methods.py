"""
What is a Class Method?
- A method that takes `cls` as the first argument instead of `self`.
- It belongs to the class itself, not the instance.
- Can access/modify class-level data.

Define using: @classmethod

What are Magic Methods?
- Also called dunder methods (double underscore), like `__init__`, `__str__`, `__len__`, etc.
- Automatically invoked for specific operations (e.g., object printing, addition, comparison).
"""

# Class Method Example
class User:
    count = 0  # class-level attribute

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def get_user_count(cls):
        return f"Total users: {cls.count}"

    @classmethod
    def from_string(cls, user_str):
        name = user_str.split("-")[0]
        return cls(name)


def class_method_demo():
    print("Class Method Demo")
    u1 = User("Alice")
    u2 = User.from_string("Bob-Admin")
    print(u1.name, "|", u2.name)
    print(User.get_user_count())
    print("-" * 40)


# Magic Method Examples
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ₹{self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


def magic_method_demo():
    print("Magic Method Demo")
    p1 = Product("Laptop", 60000)
    p2 = Product("Monitor", 20000)
    p3 = Product("Laptop", 60000)

    print("__str__:", p1)            # triggers __str__
    print("__add__:", p1 + p2)       # triggers __add__
    print("__eq__:", p1 == p3)       # triggers __eq__
    print("-" * 40)


# ML Use Case: Dataset with __len__ and __getitem__
class Dataset:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


def ml_magic_method_demo():
    print("ML Use Case: Dataset-like class")
    ds = Dataset([10, 20, 30, 40, 50])
    print("Length:", len(ds))           # __len__
    print("Item at index 2:", ds[2])    # __getitem__
    print("-" * 40)


def main():
    """
    Run all class method and magic method demos
    """
    class_method_demo()
    magic_method_demo()
    ml_magic_method_demo()


if __name__ == "__main__":
    main()
