### 1. Recursive Function

def count_down(num):
    if num <= 0:
        print("Dead end")
        return
    print("num:", num)
    count_down(num - 1)

# Calling the function
count_down(10)



### 2. OS Module (Operating System Module)

import os
import shutil

# Get current working directory
print("Current Working Directory:", os.getcwd())

# List directory contents
print("Directory Contents:", os.listdir())

# Create a directory named "test"
os.mkdir("test")

# Rename "test" directory to "test_new"
os.rename("test", "test_new")

# Remove "test_new" directory
os.rmdir("test_new")

# Remove an entire directory (if it exists)
shutil.rmtree("Example Folder", ignore_errors=True)

# Check if a directory exists
print("Does 'test_new' exist?", os.path.isdir("test_new"))



### 3. File I/O (Input/Output)

# Writing to a file
file = open("text.txt", "w")
file.write("Ramzan Mubarak")
file.close()

# Reading from a file
file = open("text.txt", "r")
print("File Content:", file.read())
file.close()

# Appending to a file
file = open("text.txt", "a")
file.write("\nRamzan Mubarak")
file.close()

# Using 'with' statement for safe file handling
with open("text.txt", "r") as file:
    print("File Content:", file.read())

### 4. Generator Function (Homework)
def my_generator():
    for i in range(500):
        yield i  # Yielding values from 0 to 499

# Call the generator
gen = my_generator()  

# Fetch the first value
print(next(gen))  # Output: 0

# Fetch the second value
print(next(gen))  # Output: 1


### 5. List Comprehension

# Given list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

# Square of each number (Normal Loop)
sqr_list = []
for num in nums:
    sqr_list.append(num * num)
print("Squares using loop:", sqr_list)

# Square of each number (List Comprehension)
sqr_list = [num * num for num in nums]
print("Squares using list comprehension:", sqr_list)

# Extract even numbers using list comprehension
even_list = [num for num in nums if num % 2 == 0]
print("Even Numbers:", even_list)
