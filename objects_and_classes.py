"""
What is a Class?
- A blueprint for creating objects.
- Contains attributes (data) and methods (functions).

What is an Object?
- An instance of a class.
- Has its own unique data based on the class definition.

Why Use OOP?
- Organize code logically and reuse it efficiently.
- Model real-world entities like User, Product, Transaction, etc.
- Essential in API design, business logic, ML models, etc.
"""

# Define a simple class
class User:
    # Class variable (shared across instances)
    platform = "PythonApp"

    # Constructor (called when object is created)
    def __init__(self, name, email):
        self.name = name        # Instance variable
        self.email = email

    # Method (acts on object)
    def greet(self):
        return f"Hello, {self.name}!"

    # Method to update email
    def update_email(self, new_email):
        self.email = new_email
        return f"Email updated to {self.email}"


def object_creation_demo():
    """
    Create objects and access attributes/methods
    """
    print("Object Creation & Access:")
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    print(user1.greet())
    print(user2.greet())
    print("Shared platform:", user1.platform)

    print(user1.update_email("alice@python.dev"))
    print("-" * 40)


# Class with __str__ override
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, ₹{self.price})"


def special_method_demo():
    """
    Demonstrate __str__ method for user-friendly output
    """
    print("Special Methods:")
    p = Product("Laptop", 75000)
    print(p)  # Automatically calls __str__()
    print("-" * 40)


# Inheritance Example
class Admin(User):  # Admin is a subclass of User
    def delete_user(self, user):
        return f"{user.name} has been deleted by Admin."


def inheritance_demo():
    """
    Inheritance demo: reuse & extend base class
    """
    print("Inheritance Demo:")
    admin = Admin("SuperAdmin", "admin@site.com")
    normal_user = User("Charlie", "charlie@web.com")

    print(admin.greet())
    print(admin.delete_user(normal_user))
    print("-" * 40)


# Real-world ML example: ModelConfig
class ModelConfig:
    def __init__(self, name, learning_rate, epochs):
        self.name = name
        self.learning_rate = learning_rate
        self.epochs = epochs

    def summary(self):
        return (f"Model: {self.name}, "
                f"Learning Rate: {self.learning_rate}, "
                f"Epochs: {self.epochs}")


def ml_model_config_demo():
    """
    ML-style example using a config class
    """
    print("ML Model Configuration:")
    cnn = ModelConfig("CNN", 0.001, 20)
    print(cnn.summary())
    print("-" * 40)


def main():
    """
    Run all object & class demos
    """
    object_creation_demo()
    special_method_demo()
    inheritance_demo()
    ml_model_config_demo()


if __name__ == "__main__":
    main()
