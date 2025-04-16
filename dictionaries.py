"""
What is a Dictionary?
- A dictionary is an unordered, mutable collection of key-value pairs.
- Keys are unique and used to retrieve values quickly (like a real dictionary).
- Think of it as a JSON object or a hashmap.

Why Dictionaries?
- Fast lookups by key.
- Ideal for structured data (e.g., user profile, config, API response).
- Widely used in ML for label mapping, config, model metadata.
"""

def create_and_access():
    """
    Creating dictionaries and accessing values by key.
    """
    user = {
        "name": "Alice",
        "age": 28,
        "email": "alice@example.com"
    }

    print("Dictionary:", user)
    print("Name:", user["name"])
    print("Age:", user.get("age"))  # safe access
    print("Phone (default):", user.get("phone", "N/A"))
    print("-" * 40)


def modify_dictionary():
    """
    Adding, updating, and deleting key-value pairs.
    """
    config = {"host": "localhost", "port": 8080}

    config["debug"] = True  # Add new key
    config["port"] = 9090   # Update existing key
    print("After update:", config)

    del config["host"]     # Remove a key
    config.pop("debug")    # Another way to remove
    print("After deletion:", config)

    config.clear()         # Remove all items
    print("After clear():", config)
    print("-" * 40)


def looping_dictionary():
    """
    Loop through keys, values, and key-value pairs.
    """
    person = {"name": "Bob", "city": "Pune", "age": 30}

    print("Looping through keys:")
    for key in person:
        print(key)

    print("Looping through values:")
    for value in person.values():
        print(value)

    print("Looping through items:")
    for key, value in person.items():
        print(f"{key}: {value}")
    print("-" * 40)


def dictionary_methods():
    """
    Useful dictionary methods.
    """
    user = {"username": "root", "role": "admin"}

    print("Keys:", user.keys())
    print("Values:", user.values())
    print("Items:", user.items())

    # setdefault(): insert default if key is missing
    user.setdefault("active", True)
    print("After setdefault:", user)

    # update(): merge another dict
    user.update({"role": "superadmin", "theme": "dark"})
    print("After update:", user)
    print("-" * 40)


def dict_comprehension():
    """
    Dictionary comprehension: generate dict dynamically.
    """
    squares = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, ...}
    evens = {x: True for x in range(10) if x % 2 == 0}
    print("Squares dict:", squares)
    print("Evens dict:", evens)
    print("-" * 40)


def real_world_use_cases():
    """
    Real-world examples for Backend & ML.
    """
    # Backend: Simulate a JSON response from an API
    response = {
        "status": 200,
        "message": "Success",
        "data": {"id": 101, "name": "API User"}
    }
    print("API Response:", response)

    # ML: Label encoding
    labels = ["cat", "dog", "fish"]
    label_map = {label: i for i, label in enumerate(labels)}
    print("Label mapping (ML):", label_map)
    print("-" * 40)


def main():
    """
    Run all dictionary-related demonstrations.
    """
    create_and_access()
    modify_dictionary()
    looping_dictionary()
    dictionary_methods()
    dict_comprehension()
    real_world_use_cases()


if __name__ == "__main__":
    main()
