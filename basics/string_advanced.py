"""
This script demonstrates:
1. String immutability
2. Escape characters
3. Multiline strings in Python
"""

def string_immutability():
    """
    Demonstrates that strings are immutable in Python.
    Once created, a string cannot be changed — only replaced.
    """
    original = "Hello"
    print("🔹 Original string:", original)

    try:
        # Trying to change a character in the string directly (will raise error)
        original[0] = "h"
    except TypeError as e:
        print("🚫 Strings are immutable! You cannot modify them directly.")
        print("Error:", e)

    print("-" * 40)

    # You can create a new string instead
    modified = "h" + original[1:]
    print("✅ Modified string (new):", modified)
    print("-" * 40)

def escape_characters():
    """
    Demonstrates usage of escape characters to handle special cases in strings.
    """
    print("🔹 Escape Characters Examples:")
    print("Newline:\nThis is on a new line")
    print("Tab:\tThis is tabbed")
    print("Backslash: This is a backslash: \\")
    print("Double quote: He said, \"Python is awesome!\"")
    print("Single quote: It\'s easy to use Python.")
    print("-" * 40)

def multiline_strings():
    """
    Demonstrates multiline strings using triple quotes.
    Useful for storing long text or documentation.
    """
    print("🔹 Multiline String:")
    message = """Dear Python Learner,

This is a multiline message.
You can use triple quotes to span text across multiple lines.

Happy Coding!
"""
    print(message)
    print("-" * 40)

def main():
    """Main function to demonstrate advanced string features."""
    string_immutability()
    escape_characters()
    multiline_strings()

if __name__ == "__main__":
    main()
