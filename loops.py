"""
This script demonstrates all types of loops in Python:
for loop, while loop, break/continue, else block with loops, nested loops, and advanced techniques.
"""

def for_loop_example():
    """Basic for loop with range."""
    print("🔹 for loop from 1 to 5:")
    for i in range(1, 6):
        print(f"Value: {i}")
    print("-" * 40)

def while_loop_example():
    """Basic while loop."""
    print("🔹 while loop from 5 down to 1:")
    count = 5
    while count > 0:
        print(f"Count: {count}")
        count -= 1
    print("-" * 40)

def break_continue_example():
    """Demonstrates break and continue."""
    print("🔹 break and continue:")
    for i in range(1, 6):
        if i == 3:
            print("Skipping 3 using continue")
            continue
        if i == 5:
            print("Breaking at 5")
            break
        print(f"Number: {i}")
    print("-" * 40)

def else_with_loop():
    """Demonstrates else clause with loop."""
    print("🔹 for-else usage (no break → else runs):")
    for i in range(3):
        print(f"Trying: {i}")
    else:
        print("Loop completed without break")
    print("-" * 40)

def nested_loop_example():
    """Nested for loops (multiplication table)."""
    print("🔹 Nested loop (Multiplication Table 1 to 3):")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} * {j} = {i * j}")
    print("-" * 40)

def loop_with_enumerate():
    """Looping with index using enumerate()."""
    print("🔹 enumerate() example:")
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    print("-" * 40)

def loop_with_zip():
    """Looping multiple sequences together using zip()."""
    print("🔹 zip() example:")
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 95]
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")
    print("-" * 40)

def main():
    """Main function to run all loop demos."""
    for_loop_example()
    while_loop_example()
    break_continue_example()
    else_with_loop()
    nested_loop_example()
    loop_with_enumerate()
    loop_with_zip()

if __name__ == "__main__":
    main()
