"""
What is Polymorphism?
- Poly = many, Morph = forms
- The same method name or interface behaves differently for different classes.

Why Use It?
- Simplifies code structure.
- Promotes flexibility and extendability.
- Enables dynamic method dispatching.

How It's Done in Python:
1. Method overriding (runtime polymorphism)
2. Duck typing (dynamic typing: "if it walks like a duck...")
"""


# Example 1: Method Overriding (Classic Polymorphism)
class Animal:
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def method_override_demo():
    print("Method Overriding Demo")
    animals = [Dog(), Cat(), Animal()]

    for animal in animals:
        print(animal.speak())  # same method, different behavior
    print("-" * 40)


# Example 2: Duck Typing (Dynamic Polymorphism)
class PDFReport:
    def generate(self):
        return "PDF report generated"


class ExcelReport:
    def generate(self):
        return "Excel report generated"


def duck_typing_demo():
    print("Duck Typing Demo")

    def generate_report(report_generator):
        print(report_generator.generate())

    pdf = PDFReport()
    excel = ExcelReport()

    generate_report(pdf)
    generate_report(excel)
    print("-" * 40)


# Real-World Example: Payment Gateway Interfaces
class Stripe:
    def process_payment(self, amount):
        return f"Processed ₹{amount} via Stripe"


class Razorpay:
    def process_payment(self, amount):
        return f"Processed ₹{amount} via Razorpay"


def payment_gateway_demo():
    print("Real-World Use Case: Payment Processing")

    def handle_payment(gateway, amount):
        print(gateway.process_payment(amount))

    stripe = Stripe()
    razorpay = Razorpay()

    handle_payment(stripe, 1000)
    handle_payment(razorpay, 2500)
    print("-" * 40)


# ML Example: Different Models with same API
class LogisticRegressionModel:
    def train(self):
        return "Training Logistic Regression"


class DecisionTreeModel:
    def train(self):
        return "Training Decision Tree"


def ml_model_polymorphism():
    print("ML Polymorphism: Unified Train Interface")
    models = [LogisticRegressionModel(), DecisionTreeModel()]

    for model in models:
        print(model.train())
    print("-" * 40)


def main():
    """
    Run all polymorphism examples
    """
    method_override_demo()
    duck_typing_demo()
    payment_gateway_demo()
    ml_model_polymorphism()


if __name__ == "__main__":
    main()
