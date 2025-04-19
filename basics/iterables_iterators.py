"""
What is an Iterable?
- Any object capable of returning its members one at a time.
- Examples: list, tuple, dict, set, str, range, file, etc.
- Anything usable in a `for` loop is an iterable.

What is an Iterator?
- An object that keeps track of where it is during iteration.
- Must implement `__iter__()` and `__next__()` methods.
- Created using the built-in `iter()` function.

Why does this matter?
- Helps build memory-efficient pipelines.
- Critical in streaming data, reading large files, or custom loop logic.
"""


def basic_iterables():
    """
    Examples of common iterables.
    """
    sample_list = [10, 20, 30]
    sample_string = "hello"
    sample_dict = {"a": 1, "b": 2}

    print("List is iterable:", hasattr(sample_list, "__iter__"))
    print("String is iterable:", hasattr(sample_string, "__iter__"))
    print("Dict is iterable:", hasattr(sample_dict, "__iter__"))
    print("-" * 40)


def convert_to_iterator():
    """
    Convert iterable to iterator using `iter()`.
    - Use `next()` to manually access items one-by-one.
    """
    nums = [1, 2, 3]
    itr = iter(nums)

    print("Accessing with next():")
    print(next(itr))
    print(next(itr))
    print(next(itr))

    try:
        print(next(itr))  # Will raise StopIteration
    except StopIteration:
        print("Iteration complete!")
    print("-" * 40)


def custom_iterator_class():
    """
    Create a custom iterator class.
    - Implements __iter__() and __next__().
    """

    class Countdown:
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            value = self.current
            self.current -= 1
            return value

    print("Custom Countdown Iterator:")
    for num in Countdown(5):
        print(num)
    print("-" * 40)


def loop_through_iterables():
    """
    Iterating through different iterable types.
    """
    print("Looping over string:")
    for ch in "abc":
        print(ch)

    print("Looping over dict keys:")
    for key in {"x": 10, "y": 20}:
        print(key)
    print("-" * 40)


def generator_function_example():
    """
    Generator = lazy iterator using `yield`.
    - Useful for large/streamed data processing.
    """

    def count_up_to(max_val):
        count = 1
        while count <= max_val:
            yield count
            count += 1

    print("Generator Example:")
    gen = count_up_to(3)
    for val in gen:
        print(val)
    print("-" * 40)


def real_world_use_cases():
    """
    Real-world examples using iterables and iterators.
    """
    # Backend: read file line by line
    print("Reading a file line-by-line (memory efficient):")
    try:
        with open("sample.txt", "w") as f:
            f.write("line1\nline2\nline3")

        with open("sample.txt") as f:
            for line in f:
                print("Read line:", line.strip())
    except Exception as e:
        print("Error with file:", e)

    # ML: Lazy data batch generator
    def batch_data(data, batch_size):
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]

    features = list(range(10))
    print("Data batches:")
    for batch in batch_data(features, 3):
        print(batch)
    print("-" * 40)


def main():
    """
    Run all examples.
    """
    basic_iterables()
    convert_to_iterator()
    custom_iterator_class()
    loop_through_iterables()
    generator_function_example()
    real_world_use_cases()


if __name__ == "__main__":
    main()
