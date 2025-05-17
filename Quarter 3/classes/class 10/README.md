# 📚 Class 10 – Python OOP Concepts Summary

This class covered several key object-oriented programming (OOP) concepts in Python including **abstraction**, **inheritance (single & multiple)**, **method resolution order (MRO)**, **dunder/magic methods**, and **class vs instance attributes**.

---

## ✅ Topics Covered

### 1. **Abstraction with ABC (Abstract Base Class)**

* `Father` is an abstract class (inherits from `ABC`).
* Uses the `@abstractmethod` decorator to define `work()` which **must be implemented** by subclasses.

```python
from abc import ABC, abstractmethod
```

### 2. **Single Inheritance**

* `Son` inherits from `Father` and implements the abstract method `work()`.
* Also has its own method `greet()`.

### 3. **Additional Inheritance**

* `Relative` also inherits from `Father` and overrides `work()`.

### 4. **Multiple Inheritance**

* `Person` inherits from both `Son` and `Relative`.
* Uses `super().__init__()` to call constructors in the correct order using **MRO**.
* The method resolution order can be checked with:

```python
print(Person.__mro__)
```

### 5. **Instance Behavior**

```python
pers = Person("Okasha", 18, "H.A", "Cousin", "G223")
```

* Calls methods from the first class in the MRO (`Son`) when there is a conflict.
* Can access inherited methods like `family()` from `Father`.

---

## ✨ Dunder (Magic) Methods

### `__init__`, `__add__`, and `__str__`

* **`__add__`**: Overloads the `+` operator to combine two `Person` instances by name and age.
* **`__str__`**: Provides a custom string representation for the object.

```python
P1 + P2  # Triggers __add__ and returns a new Person
print(P1)  # Triggers __str__
```

---

## 🏫 Class vs Instance Attributes

### Class: `Student`

* **Class-level attribute**: `school_name`
* **Instance attributes**: `name`, `grade`, `language`
* **Class method**: `change_school()` to update class-level attribute.

```python
Student.school_name = "Future Vision Academy"
Student.change_school("Knowledge House School")
```

---

## 🧠 Key Learnings

* Use `ABC` and `@abstractmethod` to define abstract classes.
* Understand inheritance hierarchies and method overriding.
* Master **multiple inheritance** and **MRO** to resolve ambiguity.
* Learn to overload operators with dunder methods (`__add__`, `__str__`).
* Know the difference between class and instance attributes.
* Utilize `@classmethod` to change shared class-level data.


