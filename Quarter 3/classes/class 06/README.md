## 🧠 Class 06 – Real-World Example, Decorators, and Special Variables (By Sir Ameen)

In this class, Sir Ameen introduced us to some important real-world practices and deeper Python concepts.

---

### 📦 Managing Project Dependencies with `requirements.txt`

- When working on a project that involves installing multiple Python libraries, it can be difficult to remember or share which libraries were installed.
- To solve this, it's a good practice to create a file named **`requirements.txt`** where you list all the libraries used in your project.
- Once the file is ready, you or anyone else can install all the required libraries using the following command:

```bash
pip install -r requirements.txt
```

> ✅ **Note:** Don’t forget the `-r` before the filename!

---

### 🧩 Python Decorators

- We learned about **decorators**, a powerful tool in Python.
- A **decorator** allows you to add new functionality to an existing function without changing its source code.
- Common use cases include logging, authentication, measuring execution time, etc.

---

### 🧪 `__test__` and 📦 `__all__` in Python

#### 🔍 `__test__`
- `__test__` is a special dictionary used by Python’s testing framework `doctest`.
- You can define test cases within this dictionary to test small pieces of code.

#### 📚 `__all__`
- `__all__` is a list that defines what is exported when `from module import *` is used.
- It helps control what should be publicly accessible from a module and hides the rest.

Example:
```python
__all__ = ['function1', 'ClassA']  # Only these will be imported when using *
```
