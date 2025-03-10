# Python Class 3 - Concepts and Examples

## Introduction
In this class, we explored several important Python concepts, including error handling, conditional statements, higher-order functions, lambda functions, and the `reduce()` function. Below is a detailed explanation of each topic covered, along with relevant examples.

---

## **1. Error Handling**
### **What is Error Handling?**
Error handling allows us to handle runtime errors gracefully, preventing our program from crashing. We use `try`, `except`, and `finally` to catch and manage errors.

### **Example:**
```python
# List of dishes
dishes = ["samose", "pakore", "chat"]
print(dishes[0])  # Output: samose

# This would cause an IndexError, so we handle it using try-except
try:
    print(dishes[4])  # Trying to access an out-of-range index
except Exception as err:
    print("Error is:", err)
print("Work done")  # This will execute
```

### **Handling Division by Zero**
```python
num = 10
try:
    print(num / 0)  # Division by zero error
except ZeroDivisionError as e:
    print("Error is:", e)
finally:
    print("Something went wrong")
```

---

## **2. Conditional Statements**
Conditional statements allow us to execute different blocks of code based on conditions.

### **Example:**
```python
isRaining = True

if isRaining:
    print("School chalo.")
else:
    print("School ki chutti")
```

### **Shorter Syntax (Ternary Operator)**
```python
print("School ki chutti") if isRaining else print("School chalo.")
```

---

## **3. Higher-Order Functions**
A higher-order function is a function that takes another function as an argument or returns a function as output.

### **Using a Function to Transform a List**
```python
numbers = [1, 2, 3, 4, 5, 6]
new_list = []

def square(num):
    return num * num

for num in numbers:
    new_list.append(square(num))

print(new_list)  # Output: [1, 4, 9, 16, 25, 36]
```

### **Using `map()` to Apply a Function to a List**
```python
numbers = [1, 2, 3, 4, 5, 6]
def square(num):
    return num * num

sqr_list = list(map(square, numbers))
print(sqr_list)  # Output: [1, 4, 9, 16, 25, 36]
```

### **Using `filter()` to Select Elements from a List**
```python
numbers = [1, 2, 3, 4, 5, 6]
def filter_cond(num):
    return num > 3

filter_list = list(filter(filter_cond, numbers))
print(filter_list)  # Output: [4, 5, 6]
```

---

## **4. Lambda Functions**
Lambda functions are anonymous functions that can be defined in a single line.

### **Example:**
```python
def add(x, y):
    return x + y
print(add(4, 7))  # Output: 11

sqr = lambda x: x * x
print(sqr(2))  # Output: 4
```

### **Using Lambda with `map()`**
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### **Using Lambda with `filter()`**
```python
numbers = [1, 2, 3, 4, 5, 6]
greater_than_three = list(filter(lambda x: x > 3, numbers))
print(greater_than_three)  # Output: [4, 5, 6]
```

---

## **5. `reduce()` Function**
The `reduce()` function, found in the `functools` module, applies a function cumulatively to a list, reducing it to a single value.

### **Example 1: Using `reduce()` to Find the Sum of a List**
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

total_sum = reduce(add, numbers)
print(total_sum)  # Output: 15 (1+2+3+4+5)
```

### **Example 2: Using `reduce()` to Multiply All Elements**
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5)
```

### **Example 3: Finding the Maximum Value in a List**
```python
from functools import reduce
numbers = [10, 24, 5, 87, 50]

max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 87
```

---

## **Conclusion**
In this class, we learned about:
✅ **Error Handling** (`try`, `except`, `finally`)
✅ **Conditional Statements** (`if-else`, ternary operator)
✅ **Higher-Order Functions** (`map()`, `filter()`)
✅ **Lambda Functions** (anonymous functions)
✅ **The `reduce()` Function** (combining values in a list)

These concepts are essential for writing efficient and robust Python programs. 🚀 Keep practicing, and happy coding! 🎯


in todays class we will learn about 

error handeling 

short hand if else / ternary 

higher order functions

lambda functions

recursion 

enumrated