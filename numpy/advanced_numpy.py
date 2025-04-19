"""
Covers:
- Advanced slicing
- Axis operations
- Boolean masking
- Broadcasting
- Random sampling
- Stacking & splitting
"""

import numpy as np

# Advanced Slicing & Fancy Indexing
def slicing_and_indexing():
    print("Fancy Indexing & Slicing")

    arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    print("Original:\n", arr)

    print("2nd row:", arr[1])
    print("Last column:", arr[:, -1])
    print("Top-left 2x2:\n", arr[:2, :2])
    print("Diagonal:", arr[[0, 1, 2], [0, 1, 2]])  # Diagonal
    print("-" * 40)


# Broadcasting (auto shape alignment)
def broadcasting_demo():
    print("Broadcasting Example")

    a = np.array([[1], [2], [3]])     # shape (3, 1)
    b = np.array([10, 20, 30])        # shape (3,)

    print("a shape:", a.shape)
    print("b shape:", b.shape)

    result = a + b                   # auto-broadcasts b
    print("a + b:\n", result)
    print("-" * 40)


# Boolean Masking & Filtering
def boolean_masking():
    print("Boolean Masking")

    arr = np.array([5, 10, 15, 20, 25])
    mask = arr > 12
    print("Mask:", mask)
    print("Filtered:", arr[mask])  # get values > 12
    print("Even numbers:", arr[arr % 2 == 0])
    print("-" * 40)


# Axis-Based Operations
def axis_operations():
    print("Axis Operations")

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Sum by row (axis=1):", np.sum(arr, axis=1))
    print("Mean by column (axis=0):", np.mean(arr, axis=0))
    print("-" * 40)


# Stack, Split, Reshape
def stacking_and_splitting():
    print("Stack & Split")

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Stack vertically:\n", np.vstack([a, b]))
    print("Stack horizontally:\n", np.hstack([a, b]))

    matrix = np.array([[1, 2], [3, 4]])
    print("Split rows:", np.vsplit(matrix, 2))
    print("Split cols:", np.hsplit(matrix, 2))
    print("-" * 40)


# Random Numbers for ML
def random_numbers_demo():
    print("Random Sampling")

    np.random.seed(42)

    print("Random integers:\n", np.random.randint(1, 100, size=(2, 3)))
    print("Random floats:\n", np.random.rand(2, 3))
    print("Normal dist:\n", np.random.normal(loc=0, scale=1, size=(2, 3)))
    print("-" * 40)


# Performance Tip: Vectorization vs Loop
def performance_demo():
    print("Performance Demo (Vectorization)")

    data = np.arange(1_000_000)

    # Vectorized
    squared = data ** 2
    print("First 5 squared:", squared[:5])

    # Equivalent using loop (slower)
    squared_list = [x ** 2 for x in data]
    print("Loop-based match:", squared_list[:5] == squared[:5].tolist())
    print("-" * 40)


def main():
    """
    Run all advanced NumPy features
    """
    slicing_and_indexing()
    broadcasting_demo()
    boolean_masking()
    axis_operations()
    stacking_and_splitting()
    random_numbers_demo()
    performance_demo()


if __name__ == "__main__":
    main()
