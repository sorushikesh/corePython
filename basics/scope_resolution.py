"""
What is Variable Scope?
- Scope defines where a variable is accessible in your code.
- Python uses LEGB Rule to resolve variable names.

LEGB Rule (Scope Resolution Order):
1. L → Local (inside function)
2. E → Enclosing (outer functions if nested)
3. G → Global (module level)
4. B → Built-in (provided by Python)

Why It's Important?
- Prevents accidental overwrites.
- Crucial in debugging, closures, decorators, and nested functions.
"""

# Global Variable
version = "1.0.0"  # Global scope


def local_scope_demo():
    """
    Local scope: variables defined inside a function.
    """
    name = "Rushikesh"  # Local to this function
    print("Inside local_scope_demo:", name)


def enclosing_scope_demo():
    """
    Enclosing scope: outer function's variable accessible to inner function.
    """
    message = "Outer"

    def inner():
        print("Inner accessing enclosing variable:", message)

    inner()


def global_scope_demo():
    """
    Access and modify global variables using 'global' keyword.
    """
    global version
    print("Original global version:", version)
    version = "2.0.0"
    print("Updated global version:", version)


def built_in_scope_demo():
    """
    Built-in scope: names like `len`, `sum`, `max`, etc.
    """
    nums = [1, 2, 3]
    print("Built-in len():", len(nums))


def scope_resolution_legb():
    """
    Demonstrating LEGB scope resolution
    """
    name = "Global"

    def outer():
        name = "Enclosing"

        def inner():
            name = "Local"
            print("LEGB → Local:", name)

        inner()
        print("LEGB → Enclosing:", name)

    outer()
    print("LEGB → Global:", name)


def nonlocal_keyword_demo():
    """
    Use 'nonlocal' to modify enclosing (non-global) variable.
    """
    count = 0

    def outer():
        counter = 5

        def inner():
            nonlocal counter
            counter += 1
            print("Inner after nonlocal increment:", counter)

        inner()
        print("Outer after inner call:", counter)

    outer()


def main():
    """
    Run all scope demos.
    """
    print("\n--- Local Scope ---")
    local_scope_demo()

    print("\n--- Enclosing Scope ---")
    enclosing_scope_demo()

    print("\n--- Global Scope ---")
    global_scope_demo()

    print("\n--- Built-in Scope ---")
    built_in_scope_demo()

    print("\n--- LEGB Scope Resolution ---")
    scope_resolution_legb()

    print("\n--- nonlocal Keyword Demo ---")
    nonlocal_keyword_demo()


if __name__ == "__main__":
    main()
