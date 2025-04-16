"""
What is match-case?
- A cleaner alternative to `if-elif-else`.
- Introduced in Python 3.10.
- Supports pattern matching like in Scala, Rust, and functional languages.

Why Use It?
- Makes branching logic easier to read.
- Works well with structured data like tuples and dicts.
- Great for REST APIs, command handling, ML label classification, etc.

Syntax:
    match variable:
        case pattern1:
            # code block
        case pattern2:
            # code block
        case _:
            # default (like else)
"""

def simple_match_case():
    """
    Match single value (like switch-case)
    """
    command = "delete"

    match command.lower():
        case "create":
            print("Creating resource...")
        case "update":
            print("Updating resource...")
        case "delete":
            print("Deleting resource...")
        case _:
            print("Unknown command!")

    print("-" * 40)


def match_with_tuple():
    """
    Match tuple patterns
    """
    point = (0, 5)

    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"On Y-axis at y={y}")
        case (x, 0):
            print(f"On X-axis at x={x}")
        case (x, y):
            print(f"Point at ({x}, {y})")

    print("-" * 40)


def match_with_dict():
    """
    Match values in dict-like data (via unpacking)
    """
    user = {"role": "admin", "active": True}

    match user:
        case {"role": "admin", "active": True}:
            print("Active Admin")
        case {"role": "admin", "active": False}:
            print("Inactive Admin")
        case _:
            print("Regular user")

    print("-" * 40)


def match_with_guards():
    """
    Add conditions to patterns using 'if' (guards)
    """
    age = 25

    match age:
        case x if x < 13:
            print("Child")
        case x if x < 20:
            print("Teen")
        case x if x < 60:
            print("Adult")
        case _:
            print("Senior")

    print("-" * 40)


def real_world_use_cases():
    """
    Backend/ML real-world usage
    """
    # Backend: HTTP response code handler
    status_code = 404

    match status_code:
        case 200:
            print("OK")
        case 201:
            print("Created")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unhandled Status")

    # ML: Label classifier
    label = "spam"

    match label:
        case "spam":
            print("Blocked as spam")
        case "ham":
            print("Marked as safe")
        case _:
            print("Needs review")

    print("-" * 40)


def main():
    """
    Run all match-case examples.
    """
    simple_match_case()
    match_with_tuple()
    match_with_dict()
    match_with_guards()
    real_world_use_cases()


if __name__ == "__main__":
    main()
