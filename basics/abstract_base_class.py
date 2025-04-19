"""
What is an Abstract Base Class?
- A class that cannot be instantiated directly.
- Defines a common interface (structure) for all subclasses.
- Enforces that certain methods must be implemented by child classes.

Why Use It?
- Create consistent APIs across multiple subclasses.
- Avoid incomplete or buggy subclass implementations.
- Essential in frameworks, ML pipelines, database drivers, etc.

Defined using: `abc` module
"""

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class implementing Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius2

    def perimeter(self):
        from math import pi
        return 2 * pi * self.radius


def shape_demo():
    print("Abstract Base Class Demo")
    r = Rectangle(10, 5)
    c = Circle(7)

    for shape in [r, c]:
        print(f"{shape.__class__.__name__} → Area: {shape.area()} | Perimeter: {shape.perimeter()}")

    try:
        s = Shape()  # 🚫 This will raise an error
    except TypeError as e:
        print("Error:", e)
    print("-" * 40)


# ML Use Case: Abstract Base for ML models
class BaseModel(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, input_data):
        pass


class LogisticRegression(BaseModel):
    def train(self, data):
        return f"Training LogisticRegression on {len(data)} samples."

    def predict(self, input_data):
        return f"Predicting using LogisticRegression for {input_data}"


class DecisionTree(BaseModel):
    def train(self, data):
        return f"Training DecisionTree on {len(data)} samples."

    def predict(self, input_data):
        return f"Predicting using DecisionTree for {input_data}"


def ml_abc_demo():
    print("ML Use Case: Abstract Base Model")
    models = [LogisticRegression(), DecisionTree()]
    data = [1, 2, 3, 4]

    for model in models:
        print(model.train(data))
        print(model.predict(5))

    print("-" * 40)


def main():
    """
    Run all Abstract Base Class demos
    """
    shape_demo()
    ml_abc_demo()


if __name__ == "__main__":
    main()
