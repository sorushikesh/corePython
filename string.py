"""
This script demonstrates how to work with strings in Python.
Includes creation, indexing, slicing, common operations, and methods.
"""

def string_basics():
    """Demonstrates basic string creation and indexing.
    [start : end : step]
    """
    name = "PythonProgramming"
    print("🔹 Original string:", name)
    print("First character:", name[0])
    print("Last character:", name[-1])
    print("Substring [0:6]:", name[0:6])  # 'Python'
    print("Every second character:", name[::2])
    print("-" * 40)

def string_operations():
    """Demonstrates common string operations."""
    str1 = "Hello"
    str2 = "World"
    print("🔹 Concatenation:", str1 + " " + str2)
    print("🔹 Repetition:", str1 * 3)
    print("🔹 Length:", len(str1))
    print("🔹 Membership check ('e' in str1):", 'e' in str1)
    print("-" * 40)

def string_methods():
    """Demonstrates commonly used string methods."""
    text = "  Python is Fun!  "
    print("🔹 Original:", repr(text))
    print("Lowercase:", text.lower())
    print("Uppercase:", text.upper())
    print("Title case:", text.title())
    print("Stripped:", text.strip())
    print("Replace:", text.replace("Fun", "Powerful"))
    print("Split:", text.split())
    print("-" * 40)

def string_formatting():
    """Demonstrates different ways to format strings."""
    lang = "Python"
    version = 3.13

    print("🔹 Formatting with f-string:")
    print(f"{lang} version is {version}")

    print("🔹 Formatting with format():")
    print("{} version is {}".format(lang, version))

    print("🔹 Old-style formatting:")
    print("%s version is %.2f" % (lang, version))

    print("-" * 40)

def iterate_string():
    """Demonstrates looping through a string."""
    word = "Hi!"
    print("🔹 Looping through:", word)
    for char in word:
        print(f"Character: {char}")
    print("-" * 40)

def main():
    """Main function to demonstrate all string examples."""
    string_basics()
    string_operations()
    string_methods()
    string_formatting()
    iterate_string()

if __name__ == "__main__":
    main()
