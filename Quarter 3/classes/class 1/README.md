# Python Basics - Quarter 3, Class 1

## Overview
This document serves as a guide for teaching the fundamental concepts of Python programming covered in the first class of Quarter 3. It includes basic syntax, data types, operators, control structures, and functions.

## Topics Covered

### 1. Printing Output
```python
print("hello world")
```
Used to display output in Python.

### 2. Variables and Constants
```python
name = "Okasha"
PI = 3.14
isMarried = False
```
Variables store data, and constants are values that should not be changed.

### 3. Data Types
- **String:** `string_data = "Hello World"`
- **Integer:** `number_data = 10`
- **Float:** `float_data = 10.5`
- **Boolean:** `boolean_data = True`
- **List:** `list_data = [1, 2, 3, 4, 5]`
- **Tuple:** `tuple_data = (1, 2, 3, 4, 5)`
- **Dictionary:** `dictionary_data = {"name": "Okasha", "age": 25}`
- **Set:** `set_data = {1, 2, 3, 4, 5}`
- **NoneType:** `none_data = None`

### 4. Difference Between List and Tuple
- **List:** Mutable (can be changed)
  ```python
  names1 = ["Okasha", "Ali", "Ahmed"]
  names1[0] = "Aneeq"  # Allowed
  ```
- **Tuple:** Immutable (cannot be changed)
  ```python
  names2 = ("Okasha", "Ali", "Ahmed")
  names2[0] = "Aneeq"  # Error!
  ```

### 5. Sets
Sets store unique values and do not allow indexing.
```python
nums_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
nums_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(nums_list[0])  # Allowed
print(nums_set[0])    # Error!
```

### 6. Operators
#### Arithmetic Operators
```python
print(10 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 5)  # Division
print(11 % 2)  # Modulus
print(10 ** 5) # Exponentiation
print(10 // 3) # Floor Division
```
#### Comparison Operators
```python
print(10 == 5)  # False
print(10 != 5)  # True
print(10 > 5)   # True
print(10 < 5)   # False
print(10 >= 5)  # True
print(10 <= 5)  # False
```
#### Logical Operators
```python
print(10 == 5 and 10 > 5)  # False
print(10 == 5 or 10 > 5)   # True
print(not 10 == 5)         # True
```
#### Assignment Operators
```python
x = 10
x += 5  # Equivalent to x = x + 5
```

### 7. F-Strings
Used for string interpolation.
```python
name = "Okasha"
fullName = f"My name is {name}"
print(fullName)
```

### 8. Conditional Statements
```python
age = 15
if age > 18:
    print("You are welcome")
elif age > 30:
    print("You are old")
else:
    print("You are a kid")
```

### 9. Functions
```python
def greet(name):
    print(f"Hello World from {name}")
    return "Returned from function"

returned_value = greet("Okasha")
print(returned_value)
```

### 10. Loops
#### For Loop
```python
names = ["Okasha", "Ali", "Ahmed"]
for n in names:
    print(n)
```
#### While Loop
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### 11. Generating a List of Numbers
```python
one_to_ten = list(range(1, 11))
print(one_to_ten)
```

## Summary
This session covered Python basics, including variables, data types, operators, conditionals, loops, and functions. The examples provided will help in future lessons and practice.

