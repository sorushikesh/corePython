"""
 What is a Tuple?
- A tuple is an ordered, immutable (unchangeable) collection in Python.
- Once created, you cannot modify its contents (no add, remove, or change).
- Tuples are faster and memory-efficient compared to lists.

 Why Tuples?
- Used for fixed collections like coordinates, DB records, constant configs.
- Hashable: Can be used as keys in dictionaries or elements in sets.
"""

def create_and_access():
    """
     Creating tuples and accessing elements.
    """
    empty_tuple = ()
    single_item = ("apple",)  # comma required!
    fruits = ("apple", "banana", "cherry")

    print("Tuple:", fruits)
    print("First item:", fruits[0])
    print("Last item:", fruits[-1])
    print("Slice [0:2]:", fruits[0:2])  # ('apple', 'banana')
    print("Single-item tuple:", single_item)
    print("-" * 40)


def tuple_methods():
    """
    Useful tuple methods: count, index
    """
    values = (1, 2, 2, 3, 4, 2)
    print("Count of 2:", values.count(2))
    print("Index of 3:", values.index(3))  # Returns first occurrence
    print("-" * 40)


def packing_unpacking():
    """
    Tuple packing & unpacking
    - Packing: assigning multiple values to a tuple.
    - Unpacking: extracting values from a tuple.
    """
    # Packing
    packed = ("python", 3.10, "release")
    print("Packed tuple:", packed)

    # Unpacking
    lang, version, status = packed
    print("Unpacked:", lang, version, status)

    # Use * to capture remaining items
    nums = (1, 2, 3, 4, 5)
    first, *middle, last = nums
    print("First:", first, "| Middle:", middle, "| Last:", last)
    print("-" * 40)


def nested_tuples():
    """
    Tuples can contain other tuples (or any data type).
    """
    matrix = (
        (1, 2, 3),
        (4, 5, 6)
    )
    print("Nested Tuple (Matrix):")
    for row in matrix:
        print(row)

    print("Element at (1,2):", matrix[1][2])  # Output: 6
    print("-" * 40)


def immutability_demo():
    """
    Demonstrate tuple immutability.
    - You can't modify a tuple once created.
    """
    config = ("localhost", 8080)
    print("Config tuple:", config)

    try:
        config[1] = 9090  #Will raise TypeError
    except TypeError as e:
        print("Error:", e)
    print("-" * 40)


def real_world_use_cases():
    """
    Real-world examples for Backend & ML.
    """
    # Backend: Return multiple values from a function
    def get_user_info():
        return ("John", "john@example.com", 25)

    name, email, age = get_user_info()
    print("User Info:", name, email, age)

    # ML: Store model dimensions (immutable and fixed)
    input_shape = (32, 32, 3)  # height, width, channels
    print("Model input shape:", input_shape)
    print("-" * 40)


def main():
    """
    🏁 Run all tuple demonstrations.
    """
    create_and_access()
    tuple_methods()
    packing_unpacking()
    nested_tuples()
    immutability_demo()
    real_world_use_cases()


if __name__ == "__main__":
    main()
