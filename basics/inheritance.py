"""
What is Inheritance?
- One class (child/subclass) inherits the properties and methods of another class (parent/superclass).
- Promotes code reuse, modularity, and extensibility.

Syntax:
    class ChildClass(ParentClass):
        # new or overridden methods

Why Use It?
- Avoid rewriting common logic.
- Organize code into hierarchies.
- Common in APIs, database models, ML model configs, etc.
"""

# Base Class (Parent)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f"Name: {self.name}, Email: {self.email}"

    def role(self):
        return "User"


# Derived Class (Child) → inherits from User
class Admin(User):
    def __init__(self, name, email, access_level):
        super().__init__(name, email)  # Call parent constructor
        self.access_level = access_level

    # Overriding parent method
    def role(self):
        return f"Admin - Access: {self.access_level}"

    def delete_user(self, user):
        return f"Deleted user: {user.name}"


# Another Subclass
class Guest(User):
    def role(self):
        return "Guest (Read-only)"


def single_inheritance_demo():
    print("Single Inheritance Demo")
    admin = Admin("Alice", "alice@admin.com", "Full")
    guest = Guest("Bob", "bob@guest.com")

    print(admin.get_details())
    print("Role:", admin.role())
    print(admin.delete_user(guest))

    print("\nGuest Info:")
    print(guest.get_details())
    print("Role:", guest.role())
    print("-" * 40)


# Multi-level Inheritance
class SuperAdmin(Admin):
    def suspend_user(self, user):
        return f"Suspended {user.name} temporarily."


def multilevel_inheritance_demo():
    print("Multilevel Inheritance Demo")
    super_admin = SuperAdmin("Charlie", "charlie@root.com", "Super")
    user = User("Eve", "eve@normal.com")

    print(super_admin.get_details())
    print(super_admin.role())
    print(super_admin.suspend_user(user))
    print("-" * 40)


# ML Use Case: BaseModel → CNNModel / RNNModel
class BaseModel:
    def __init__(self, name):
        self.name = name

    def train(self):
        return f"Training {self.name} model..."

    def summary(self):
        return f"{self.name} - Base model class"


class CNNModel(BaseModel):
    def summary(self):
        return f"{self.name} - Convolutional Neural Network"


class RNNModel(BaseModel):
    def summary(self):
        return f"{self.name} - Recurrent Neural Network"


def ml_model_inheritance_demo():
    print("ML Inheritance Use Case")
    cnn = CNNModel("ImageClassifier")
    rnn = RNNModel("TextAnalyzer")

    print(cnn.train())
    print(cnn.summary())

    print(rnn.train())
    print(rnn.summary())
    print("-" * 40)


def main():
    """
    Run all inheritance examples
    """
    single_inheritance_demo()
    multilevel_inheritance_demo()
    ml_model_inheritance_demo()


if __name__ == "__main__":
    main()
