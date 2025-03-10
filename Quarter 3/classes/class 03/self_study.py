# Error handeling 

# Handling Multiple Errors
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")
else:
    print(f"Result: {result}")  # Runs if no exception
finally:
    print("Execution finished!")  # Always runs


# Raising Custom Exceptions
# You can raise an error manually using raise.
# Raising an Exception 

age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("You must be 18 or older to proceed!")
# ✔️ If age = 16 → ValueError: You must be 18 or older to proceed!


# Concatenating Strings in a List (Reduce) 
from functools import reduce

words = ["Hello", "world", "this", "is", "Python"]

# Lambda function to concatenate strings
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Output: "Hello world this is Python"
