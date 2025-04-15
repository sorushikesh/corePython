"""
What is a Set?
- A set is an unordered, unindexed, and mutable collection of unique elements.
- Duplicates are automatically removed.
- Very useful when you want to store unique items (e.g., user roles, tags, features).

Why Sets?
- Fast membership checks (`in`).
- Useful for deduplication.
- Great for set operations (union, intersection, difference).
"""

def create_and_basic_operations():
    """
    Creating sets and performing basic operations.
    """
    fruits = {"apple", "banana", "cherry", "apple"}  # Duplicates are removed
    empty_set = set()  # Use set(), not {} ({} is dict)

    print("Set of fruits (unique):", fruits)
    print("Length of set:", len(fruits))

    print("Is 'banana' in set?", "banana" in fruits)
    print("-" * 40)


def modify_set():
    """
    Modifying sets using add(), update(), remove(), discard(), and pop().
    """
    languages = {"Python", "Java"}

    languages.add("C++")  # Add single element
    print("After add('C++'):", languages)

    languages.update(["Rust", "Go"])  # Add multiple elements
    print("After update([...]):", languages)

    languages.remove("Java")  # Removes element (KeyError if not found)
    print("After remove('Java'):", languages)

    languages.discard("Scala")  # Discard (no error if not found)
    print("After discard('Scala') (safe):", languages)

    removed = languages.pop()  # Removes random element (set is unordered)
    print(f"After pop(): {languages}, removed = {removed}")

    languages.clear()
    print("After clear():", languages)
    print("-" * 40)


def set_operations():
    """
    Set algebra: union, intersection, difference, symmetric_difference
    Very useful for comparing datasets.
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("Set A:", a)
    print("Set B:", b)

    print("Union (A ∪ B):", a.union(b))
    print("Intersection (A ∩ B):", a.intersection(b))
    print("Difference (A - B):", a.difference(b))
    print("Symmetric Difference (A Δ B):", a.symmetric_difference(b))
    print("-" * 40)


def set_comprehension():
    """
    Set comprehension: build a set using a condition.
    """
    squares = {x**2 for x in range(6)}
    evens = {x for x in range(10) if x % 2 == 0}

    print("Squares (set):", squares)
    print("Evens (set):", evens)
    print("-" * 40)


def real_world_use_cases():
    """
    Real-world examples for Backend & ML.
    """
    # Backend Example: Deduplicate roles
    roles = ["admin", "editor", "admin", "viewer"]
    unique_roles = set(roles)
    print("Unique user roles:", unique_roles)

    # ML Example: Unique labels in classification
    predictions = ["spam", "ham", "spam", "spam", "ham"]
    unique_classes = set(predictions)
    print("Unique predicted classes:", unique_classes)
    print("-" * 40)


def main():
    """
    Run all set-related demonstrations.
    """
    create_and_basic_operations()
    modify_set()
    set_operations()
    set_comprehension()
    real_world_use_cases()


if __name__ == "__main__":
    main()
