"""
What is `__name__`?
- A special built-in variable in every Python module.
- It represents the name of the module.

What is `__main__`?
- When a Python file is run directly, Python sets `__name__ = "__main__"`.
- If the file is imported as a module, then `__name__ = "filename"` (not `__main__`).

Why Use `if __name__ == "__main__"`?
- To separate reusable code (functions/classes) from executable code.
- Ensures that some code only runs when file is executed directly, not when imported.

Real-World Use:
- Common in scripts, CLI tools, test drivers, entry points.
"""

# Utility function
def greet(name):
    return f"Hello, {name}!"

# Test or main logic block
def run_script():
    user = "Rushikesh"
    print(greet(user))
    print("Script is running directly.")


# Guard block: entry point of the script
if __name__ == "__main__":
    run_script()
