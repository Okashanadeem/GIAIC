# Class 4 - Learning Summary

## Introduction
In this class, we covered multiple essential Python concepts, including recursion, OS module operations, file handling, generators, and list comprehensions. We learned through hands-on coding exercises, writing functions, and testing them interactively in a Jupyter Notebook.

---

## Topics Covered

### 1. Recursive Function
We explored **recursion**, which allows a function to call itself. The `count_down` function was implemented to demonstrate this concept:
```python
def count_down(num):
    if num <= 0:
        print("Dead end")
        return
    print("num:", num)
    count_down(num - 1)
```
This function repeatedly calls itself while decreasing the number until it reaches zero.

---

### 2. OS Module (Operating System Module)
We used Python's **os module** to interact with the system and perform operations like:
- Fetching the current working directory
- Listing directory contents
- Creating, renaming, and deleting folders
- Removing entire directories using `shutil`

Example operations:
```python
import os
import shutil
print("Current Directory:", os.getcwd())
os.mkdir("test")
os.rename("test", "test_new")
os.rmdir("test_new")
shutil.rmtree("Example Folder", ignore_errors=True)
```

---

### 3. File I/O (Input/Output)
We learned how to **read, write, and append files** in Python:
```python
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
```
To ensure safe file handling, we used the `with open()` statement.

---

### 4. Generator Functions (Homework)
We discussed **generator functions**, which use `yield` to produce values one at a time instead of returning them all at once. This makes them memory-efficient.

Example (to be implemented as homework):
```python
def my_generator():
    for i in range(500):
        yield i
```
Using `next()` fetches values one by one.

---

### 5. List Comprehension
We explored **list comprehension**, which provides a concise way to create lists.

Example:
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

# Squares of numbers
sqr_list = [num * num for num in nums]
print("Squares:", sqr_list)

# Even numbers
even_list = [num for num in nums if num % 2 == 0]
print("Even Numbers:", even_list)
```

---

## How We Learned
- **Hands-on coding:** We implemented concepts directly in a Jupyter Notebook.
- **Debugging and testing:** We executed and tested our code step by step.
- **Class discussions:** Concepts were reinforced through explanations and practical examples.
- **Homework assignments:** The generator function was assigned for independent practice.

---

## Conclusion
This class provided a strong foundation in recursion, OS operations, file handling, generators, and list comprehension. Through coding exercises and interactive learning, we built a deeper understanding of Python programming concepts.

---

**Happy Coding! 🚀**

