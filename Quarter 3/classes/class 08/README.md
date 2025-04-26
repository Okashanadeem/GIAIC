# Class 08 – Python Revision

In this class, we revisited several important Python concepts. Here's a structured overview:

---

## 🐍 Python Basics

- **Python** is an *interpreted* and *intelligent* language.
- The interpreter can automatically infer the type of a variable.  
  Example:
  
  ```python
  name: str = 10
  print("name:", name)
  ```

- **Type Annotations** have two main purposes:
  1. **Type Hinting** – Helps developers understand the intended data type.
  2. **Type Restriction** – Restricts a variable to a specific data type.

- **Popular Python Interpreters**:  
  - CPython (default)  
  - Jython (for Java integration)

- To enforce type checking during development, tools like **`mypy`** can be used.

---

## 📦 Python Packages

- Python offers a vast collection of libraries and packages, for example:
  - `streamlit` (for building web apps)
  - `mypy` (for static type checking)

---

## 🔀 Control Flow in Python

Control flow structures help manage the direction of program execution.

Example (using `if-else`):

```python
name = "okasha"

if name == "okasha":
    print("Hello Mister!")
else:
    print("Kon ho bhai?")
```

- **Indentation** is crucial in Python:
  - After a `:`, the code inside a block must be indented (typically 4 spaces or a tab).

- Python also supports:
  - `elif` (else-if)
  - `match-case` (introduced in Python 3.10 for pattern matching)

---

## 📚 Modules in Python

- **Modules** allow importing and exporting code between different files and projects.
- Examples of platforms we use:
  - **VS Code** (local development)
  - **Google Colab** (for running heavy code when local systems can't handle it)

---

## 🚨 Error Handling

- In Python, when an error occurs, the code **stops execution** unless handled.
- **Example scenario**:  
  If a bank software encounters a *Zero Division Error* and it’s not handled, the entire process might crash, freezing transactions.

- Python provides **`try-except` blocks** to handle such errors gracefully:

  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero!")
  ```

- This ensures that the interpreter **catches errors** and continues running the rest of the code.

---

## 🔁 Mutable vs Immutable

- **Mutable**: Can be changed (e.g., lists, dictionaries).
- **Immutable**: Cannot be changed (e.g., strings, tuples).

---

## 🎀 Decorators

- **Decorators** allow running additional code around a function.
- A decorator is also called a **wrapper function**.

Example (conceptually):
```python
def decorator_function(original_function):
    def wrapper_function():
        print("Code before the original function.")
        original_function()
        print("Code after the original function.")
    return wrapper_function
```

---

# 🚀 Summary

Today’s class was a complete revision of core Python concepts, setting a strong foundation for advanced topics ahead.
