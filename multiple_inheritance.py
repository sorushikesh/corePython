"""
What is Multiple Inheritance?
- A class can inherit from more than one parent class.
- Useful when combining features from different, independent classes.

Syntax:
    class ChildClass(Parent1, Parent2):
        pass

Why Use It?
- Reuse logic across unrelated classes.
- Combine capabilities (e.g., logging, validation, messaging).
"""

# Parent Class 1
class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")


# Parent Class 2
class Validator:
    def validate(self, data):
        return isinstance(data, dict)


# Child Class with multiple inheritance
class Service(Logger, Validator):
    def process(self, request):
        if self.validate(request):
            self.log("Processing request...")
            return "Request processed."
        else:
            self.log("Invalid request format.")
            return "Validation failed."


def basic_multiple_inheritance_demo():
    print("Multiple Inheritance: Logger + Validator")
    service = Service()
    valid_data = {"name": "Rushikesh"}
    invalid_data = "invalid"

    print(service.process(valid_data))
    print(service.process(invalid_data))
    print("-" * 40)


# Real-World Use Case: ML Training Module
class DataLoader:
    def load(self):
        return [1, 2, 3, 4]


class ModelTrainer:
    def train(self, data):
        return f"Training model on {len(data)} records..."


class MLWorkflow(DataLoader, ModelTrainer):
    def execute(self):
        data = self.load()
        result = self.train(data)
        return result


def ml_workflow_demo():
    print("ML Workflow using Multiple Inheritance")
    workflow = MLWorkflow()
    print(workflow.execute())
    print("-" * 40)


# Method Resolution Order (MRO) Demo
class A:
    def speak(self):
        print("A speaks")


class B(A):
    def speak(self):
        print("B speaks")


class C(A):
    def speak(self):
        print("C speaks")


class D(B, C):  # Inherits from B and C → B is prioritized
    pass


def mro_demo():
    print("Method Resolution Order (MRO)")
    d = D()
    d.speak()  # Output will follow MRO: D → B → C → A
    print("MRO:", [cls.__name__ for cls in D.__mro__])
    print("-" * 40)


def main():
    """
    Run all multiple inheritance examples
    """
    basic_multiple_inheritance_demo()
    ml_workflow_demo()
    mro_demo()


if __name__ == "__main__":
    main()
