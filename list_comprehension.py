"""
What is List Comprehension?
- A concise way to create or transform lists in a single line.
- More readable and faster than traditional `for` loops.

Syntax:
    [expression for item in iterable if condition]

Why Use It?
- Reduces boilerplate code.
- Improves performance.
- Commonly used in data processing, filtering, and transformation tasks.
"""

def basic_examples():
    """
    Basic usage of list comprehension
    """
    print("Squares of 1–5:")
    squares = [x**2 for x in range(1, 6)]
    print(squares)

    print("Uppercase words:")
    words = ["python", "rocks", "hard"]
    upper = [word.upper() for word in words]
    print(upper)

    print("Only even numbers:")
    evens = [x for x in range(10) if x % 2 == 0]
    print(evens)

    print("-" * 40)


def conditional_output():
    """
    Use if-else within list comprehension
    """
    print("Replace even/odd labels:")
    result = ["even" if x % 2 == 0 else "odd" for x in range(6)]
    print(result)

    print("-" * 40)


def nested_list_comprehension():
    """
    Use nested loops inside list comprehension
    """
    print("All coordinate pairs (x, y):")
    coords = [(x, y) for x in range(3) for y in range(2)]
    print(coords)

    print("Flatten 2D list:")
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [item for row in matrix for item in row]
    print(flat)

    print("-" * 40)


def real_world_use_cases():
    """
    Practical use cases for list comprehension
    """
    print("Backend: Extract user emails:")
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]
    emails = [user["email"] for user in users]
    print(emails)

    print("\nML: Filter positive samples:")
    samples = [0.3, -0.2, 0.8, -1.5, 0.9]
    positives = [x for x in samples if x > 0]
    print(positives)

    print("\nClean data: Remove nulls or empty strings:")
    raw = ["apple", "", None, "banana", " "]
    clean = [x.strip() for x in raw if x and x.strip()]
    print(clean)

    print("-" * 40)


def main():
    """
    Run all list comprehension examples.
    """
    basic_examples()
    conditional_output()
    nested_list_comprehension()
    real_world_use_cases()


if __name__ == "__main__":
    main()
