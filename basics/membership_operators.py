"""
What are Membership Operators?
- Used to test if a value is present in a sequence (like list, string, tuple, dict, set).
- They return a Boolean result: `True` or `False`.

Types:
1. `in`     → returns True if value is found
2. `not in` → returns True if value is NOT found

Why Use Them?
- Efficient checks for values in containers.
- Used in validations, data filtering, token search, etc.
"""

def basic_membership_tests():
    """
    Demonstrates `in` and `not in` on various datatypes.
    """
    print("In List:")
    numbers = [1, 2, 3, 4]
    print("3 in numbers?", 3 in numbers)
    print("10 not in numbers?", 10 not in numbers)

    print("\nIn String:")
    msg = "hello world"
    print("'world' in msg?", "world" in msg)
    print("'python' not in msg?", "python" not in msg)

    print("\nIn Tuple:")
    items = ("apple", "banana", "cherry")
    print("'banana' in tuple?", "banana" in items)

    print("\nIn Set:")
    ids = {101, 102, 103}
    print("102 in ids?", 102 in ids)

    print("\nIn Dictionary (keys only):")
    user = {"name": "Alice", "role": "admin"}
    print("'name' in user?", "name" in user)
    print("'Alice' in user.values()?", "Alice" in user.values())
    print("-" * 40)


def real_world_use_cases():
    """
    Real backend & ML use cases using membership operators.
    """
    print("Backend: Validate email domain")
    email = "user@example.com"
    allowed_domains = ["example.com", "serrala.com"]
    domain = email.split("@")[-1]

    if domain in allowed_domains:
        print("Domain is allowed")
    else:
        print("Domain not allowed")

    print("\nML: Check if label is known")
    label = "spam"
    known_labels = {"ham", "spam", "neutral"}

    if label in known_labels:
        print("Label is valid")
    else:
        print("Unknown label")
    print("-" * 40)


def main():
    """
    Run all membership operator examples.
    """
    basic_membership_tests()
    real_world_use_cases()


if __name__ == "__main__":
    main()
