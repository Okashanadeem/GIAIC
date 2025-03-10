print("hello Okasha")  # Simple print statement

# Error Handling with Try-Except
# Creating a list of dishes
dishes = ["samose", "pakore", "chat"]
print(dishes[0])  # Accessing the first element

# Uncommenting the next line would cause an IndexError because index 4 is out of range
# print(dishes[4])
# print("work done")  # This line wouldn't execute if an error occurs above

# Using try-except to handle errors
try:
    print(dishes[4])  # Attempting to access an invalid index
except Exception as err:
    print("Error is:", err)  # Catching and printing the error
    print("work done")  # This will execute even if an error occurs

# Handling ZeroDivisionError
num = 10
try:
    print(10/0)  # This will cause a ZeroDivisionError
except Exception as e:
    print("Error is:", e)

# Specific exception handling using ZeroDivisionError
try:
    print(num/0)
except ZeroDivisionError as e:  # Catching a specific error type
    print("Error is:", e)
finally:
    print("Something went wrong")  # This block executes no matter what

# Conditional Statements
isRaining = True

# Traditional if-else statement
if isRaining:
    print("School chalo.")
else:
    print("School ki chutti")

# Ternary operator (short-hand if-else)
print("School ki chutti") if not isRaining else print("School chalo.")

# Ternary assignment
num = 5
num2 = 10 if num <= num else 20  # Assigning value based on condition
print(num2)

# Higher-Order Functions
numbers = [1, 2, 3, 4, 5, 6]

# Function to square a number
def square(num):
    return num * num

# Using a for loop to apply the function
new_list = []
for num in numbers:
    sqr_num = square(num)
    new_list.append(sqr_num)
print(new_list)  # Prints squared numbers

# Using map() function to apply a function to a list
sqr_list = list(map(square, numbers))
print(sqr_list)

# Using filter() function to filter numbers greater than 3
def filter_cond(num):
    return num > 3

filter_list = list(filter(filter_cond, numbers))
print(filter_list)  # Prints numbers greater than 3

# Incorrect use of map() for filtering (returns boolean values instead of filtered numbers)
filter_list = list(map(filter_cond, numbers))
print(filter_list)  # Prints True/False values instead of filtered numbers

# TODO: Reduce function (Homework)

# Lambda Functions
# Regular function for addition
def add(x, y):
    return x + y
print(add(4, 7))

# Lambda function for squaring a number
sqr = lambda x: x * x
print(sqr(2))
