# Difference Between `return` and `yield`

def normal_func():
    """
    This function returns all values at once using `return`.
    """
    return [1, 2, 3]

print("Using return:", normal_func())  # Output: [1, 2, 3]


def generator_func():
    """
    This function generates values one by one using `yield`.
    """
    for i in range(1, 4):
        yield i  # Pauses and returns one value at a time

# Creating a generator object
gen = generator_func()

print("Using yield:")
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
