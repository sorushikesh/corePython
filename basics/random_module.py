"""
What is the `random` module?
- A built-in Python module used to generate random numbers.
- Useful in simulations, games, cryptography (basic), testing, and ML.

Why use it?
- Randomized behaviors (like generating OTPs).
- Data sampling/shuffling (important in ML model training).
- Load/stress testing and mock data generation.
"""

import random
import string


def basic_random_operations():
    """
    Generate random integers and floats.
    """
    print("Random integer between 1 and 100:", random.randint(1, 100))  # inclusive
    print("Random float [0.0, 1.0):", random.random())  # like Math.random() in JS
    print("Random float in a range:", random.uniform(10, 20))  # float between 10-20
    print("-" * 40)


def random_choice_and_sample():
    """
    Choose random elements from a list.
    """
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    print("Random name (single):", random.choice(names))      # 1 random item
    print("Random sample (3 unique):", random.sample(names, 3))  # 3 unique
    print("Random choices (3 with repetition):", random.choices(names, k=3))  # allows duplicates
    print("-" * 40)


def random_shuffle_and_seed():
    """
    Shuffle lists and use random seed for reproducibility.
    """
    items = [1, 2, 3, 4, 5]
    print("Before shuffle:", items)

    random.shuffle(items)
    print("After shuffle:", items)

    print("Using seed:")
    random.seed(42)
    print("Same random number with seed(42):", random.randint(1, 100))

    random.seed(42)
    print("Same again with seed(42):", random.randint(1, 100))  # Will match above
    print("-" * 40)


def generate_random_strings_otp():
    """
    Random strings, OTPs, and passwords.
    """
    import string_operations

    digits = string.digits
    letters = string.ascii_letters
    special = string.punctuation

    otp = ''.join(random.choices(digits, k=6))
    password = ''.join(random.choices(letters + digits + special, k=10))

    print("OTP (6 digits):", otp)
    print("Random Password:", password)
    print("-" * 40)


def ml_use_case_shuffle_split():
    """
    ML Use Case: Shuffle and split dataset into train/test
    """
    data = list(range(100))  # pretend this is your dataset
    random.shuffle(data)

    train_size = int(0.8 * len(data))
    train_data = data[:train_size]
    test_data = data[train_size:]

    print("Train data (80%):", train_data[:5], "...")  # preview
    print("Test data (20%):", test_data[:5], "...")
    print("-" * 40)


def main():
    """
    Run all random-related demonstrations.
    """
    basic_random_operations()
    random_choice_and_sample()
    random_shuffle_and_seed()
    generate_random_strings_otp()
    ml_use_case_shuffle_split()


if __name__ == "__main__":
    main()
