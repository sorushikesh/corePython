"""
  What are Lists?
- Lists are ordered, mutable (changeable) collections in Python.
- Used to store multiple values in a single variable.
- Commonly used for storing data records, results, features, etc.

  Why Lists?
- Easily group related items (e.g., usernames, scores, predictions).
- Flexible: can hold any data type, including other lists.

  Key Features:
- Ordered: Items maintain insertion order.
- Mutable: You can change, add, or remove elements.
- Indexable: You can access elements via index.
- Iterable: You can loop through them.

  Real Use Cases:
- Backend: Store rows from DB, users, request logs.
- ML: Hold datasets, features, labels, model predictions.
"""

def create_and_access():
    """
      Creating and accessing list elements.
    - Index starts at 0.
    - Negative index accesses from end.
    - Slicing gives sublist.
    """
    fruits = ["apple", "banana", "cherry", "date"]
    print("List:", fruits)
    print("First item:", fruits[0])      # "apple"
    print("Last item:", fruits[-1])      # "date"
    print("Sliced list [1:3]:", fruits[1:3])  # ['banana', 'cherry']
    print("-" * 40)


def modify_list():
    """
      Modifying lists using built-in methods.
    - append(): Adds to end.
    - extend(): Adds multiple items.
    - insert(): Adds at index.
    - remove(): Deletes specific value.
    - pop(): Deletes and returns last value.
    - index(): Finds index of value.
    - count(): Counts occurrences.
    """
    numbers = [1, 2, 3]
    print("Original list:", numbers)

    numbers.append(4)
    print("After append(4):", numbers)

    numbers.extend([5, 6])
    print("After extend([5, 6]):", numbers)

    numbers.insert(1, 10)
    print("After insert at index 1:", numbers)

    numbers.remove(3)
    print("After remove(3):", numbers)

    popped = numbers.pop()
    print(f"After pop(): {numbers} | popped value = {popped}")

    print("Index of 10:", numbers.index(10))
    print("Count of 2:", numbers.count(2))
    print("-" * 40)


def looping_through_list():
    """
      Looping through lists.
    - Use 'for' loop to access items directly.
    - Use range(len()) to access with index.
    """
    cities = ["Pune", "Mumbai", "Delhi"]
    print("Looping with for-in:")
    for city in cities:
        print("City:", city)

    print("🔹 Looping with index:")
    for i in range(len(cities)):
        print(f"{i}: {cities[i]}")
    print("-" * 40)


def sort_and_reverse():
    """
      Sorting and reversing lists.
    - sort(): Sorts in-place (ascending by default).
    - reverse(): Reverses current list.
    - sort(reverse=True): Sorts in descending order.
    """
    nums = [5, 1, 9, 3]
    print("Original list:", nums)

    nums.sort()
    print("Sorted ascending:", nums)

    nums.sort(reverse=True)
    print("Sorted descending:", nums)

    nums.reverse()
    print("Reversed list:", nums)
    print("-" * 40)


def list_comprehensions():
    """
      List comprehensions.
    - Shorter syntax for creating new lists.
    - [expression for item in iterable]
    - Optional filter: [x for x in list if condition]

    💡 Fast and Pythonic way to transform or filter data.
    """
    squares = [x ** 2 for x in range(1, 6)]  # Square numbers 1 to 5
    evens = [x for x in range(10) if x % 2 == 0]  # Even numbers < 10

    print("Squares from 1 to 5:", squares)
    print("Even numbers < 10:", evens)

    # Example: capitalize names
    names = ["alice", "bob", "charlie"]
    upper_names = [name.upper() for name in names]
    print("Uppercase names:", upper_names)
    print("-" * 40)


def nested_lists():
    """
      Nested Lists (2D Lists).
    - Lists inside lists (like matrices or tables).
    - Useful for tabular data, grids, ML datasets.

    Access via: list[row][column]
    """
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("🔹 2D List (Matrix):")
    for row in matrix:
        print(row)

    print("Element at row 1, column 2:", matrix[1][2])  # 6
    print("-" * 40)


def main():
    """
    Run all demonstrations in order.
    """
    create_and_access()
    modify_list()
    looping_through_list()
    sort_and_reverse()
    list_comprehensions()
    nested_lists()


if __name__ == "__main__":
    main()
