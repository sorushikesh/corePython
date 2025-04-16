"""
What is a Function?
- A block of reusable code that performs a specific task.
- Can accept inputs (parameters) and return outputs.
- Helps in code reuse, modularity, testing, and abstraction.

Why Functions?
- Avoid code repetition.
- Improve readability and testability.
- Used for API logic, data processing, model training, etc.
"""

# Basic Function: No arguments, no return
def greet():
    print("Hello, Developer!")

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

# Function with return value
def square(num):
    return num ** 2

# Function with default parameter
def connect_to_db(host="localhost", port=3306):
    print(f"Connecting to DB at {host}:{port}")

# Function with multiple return values (tuple)
def get_user():
    return "Alice", 30, "alice@example.com"

# Function with variable-length arguments
def log_events(*events):
    for event in events:
        print("Logged:", event)

# Function with keyword arguments
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Lambda (anonymous) function
double = lambda x: x * 2

# Function as argument (higher-order)
def operate_on_list(nums, operation):
    return [operation(n) for n in nums]

# Nested Functions
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)

# Recursion Example: Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Real Backend Example: API handler function
def get_user_profile(user_id):
    # Simulated database response
    db = {
        1: {"name": "Alice", "role": "admin"},
        2: {"name": "Bob", "role": "viewer"}
    }
    return db.get(user_id, {"error": "User not found"})

# Real ML Example: Feature normalization
def normalize_features(features):
    min_val = min(features)
    max_val = max(features)
    return [(x - min_val) / (max_val - min_val) for x in features]


def main():
    """
    Run all function examples
    """
    print("\n--- Basic Functions ---")
    greet()
    greet_user("Rushikesh")
    print("Square of 5:", square(5))

    print("\n--- Default Arguments ---")
    connect_to_db()
    connect_to_db(port=5432)

    print("\n--- Multiple Return Values ---")
    name, age, email = get_user()
    print(f"{name} | {age} | {email}")

    print("\n--- *args Example ---")
    log_events("start", "stop", "restart")

    print("\n--- **kwargs Example ---")
    print_user_info(name="Charlie", role="editor", active=True)

    print("\n--- Lambda & HOF ---")
    print("Double of 10:", double(10))
    nums = [1, 2, 3]
    print("Squares using HOF:", operate_on_list(nums, lambda x: x**2))

    print("\n--- Nested & Recursive Functions ---")
    print("Outer function result:", outer_function(5))
    print("Factorial of 5:", factorial(5))

    print("\n--- Backend/ML Use Cases ---")
    print("User Profile (id=1):", get_user_profile(2))
    features = [10, 20, 30, 40]
    print("Normalized Features:", normalize_features(features))


if __name__ == "__main__":
    main()
