"""
What is NumPy?
- The core library for **numerical computing** in Python.
- Efficient array operations, linear algebra, broadcasting, etc.

Why Use It?
- Much faster than native Python lists.
- Essential for ML (used in Pandas, Scikit-learn, TensorFlow, etc.)
"""

import numpy as np

# 1D and 2D Array Creation
def create_arrays():
    print("Creating NumPy Arrays")

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[1, 2], [3, 4]])

    print("1D array:", arr1)
    print("2D array:\n", arr2)
    print("Shape:", arr2.shape)
    print("Datatype:", arr2.dtype)
    print("-" * 40)


# Array Operations
def array_operations():
    print("Array Arithmetic")

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Add:", a + b)
    print("Multiply:", a * b)
    print("Dot Product:", np.dot(a, b))
    print("Mean:", np.mean(a))
    print("Sum:", np.sum(b))
    print("-" * 40)


# Array Indexing & Slicing
def array_indexing():
    print("Indexing & Slicing")

    mat = np.array([[10, 20, 30], [40, 50, 60]])

    print("Matrix:\n", mat)
    print("Element at (0, 1):", mat[0, 1])
    print("First row:", mat[0])
    print("First column:", mat[:, 0])
    print("-" * 40)


# Array Creation Shortcuts
def create_helper_arrays():
    print("Helper Array Functions")

    print("Zeros:\n", np.zeros((2, 3)))
    print("Ones:\n", np.ones((2, 3)))
    print("Range:\n", np.arange(0, 10, 2))
    print("Linspace:\n", np.linspace(0, 1, 5))
    print("Identity:\n", np.eye(3))
    print("-" * 40)


# Reshape, Flatten, Transpose
def reshape_and_transform():
    print("Reshape, Flatten, Transpose")

    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("Original:\n", a)

    print("Flattened:", a.flatten())
    print("Transposed:\n", a.T)
    print("Reshaped (3x2):\n", a.reshape(3, 2))
    print("-" * 40)


# Real-World ML Example: Feature Normalization
def normalize_features():
    print("ML Use Case: Feature Normalization")

    X = np.array([[100, 10], [200, 20], [300, 30]])

    X_min = X.min(axis=0)
    X_max = X.max(axis=0)

    X_scaled = (X - X_min) / (X_max - X_min)

    print("Original:\n", X)
    print("Normalized (0–1):\n", X_scaled)
    print("-" * 40)


def main():
    """
    Run all NumPy demos
    """
    create_arrays()
    array_operations()
    array_indexing()
    create_helper_arrays()
    reshape_and_transform()
    normalize_features()


if __name__ == "__main__":
    main()
