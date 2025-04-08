## 🧠 Class 5 - Python Deep Dive: Data Types, Identity, and Modern Tools

### 📚 Summary of Key Topics

#### 🔢 **1. Complex Numbers**
- A `complex` number has a real and imaginary part: `a + bj`
```python
number = 2 + 5j
number.real      # 2.0
number.imag      # 5.0
```

#### 🧮 **2. Binary Representation**
- Convert an integer to binary using `bin()`:
```python
bin(10)  # '0b1010'
```

#### 📁 **3. Reading Binary Files**
- Use `"rb"` mode to read files like images:
```python
with open("pythoned.png", "rb") as file:
    data = file.read()
```

#### 🆔 **4. Object Identity & Comparison**
- Use `id()` to check memory address.
- `is` checks **identity**, `==` checks **equality**.
```python
list_one is list_two    # False
list_one == list_two    # True
```

#### 🧵 **5. String Interning**
- Python stores identical strings in one memory spot.
```python
a = "Hello"
b = "Hello"
id(a) == id(b)  # True
```

#### 🔥 **6. Interning Beyond Limits**
- Numbers above 256 might not share memory:
```python
a = 257
b = 257
a is b  # False (sometimes)
```

#### 📦 **7. `sys.intern()`**
- Force intern strings manually:
```python
from sys import intern
x = intern("This is a long string")
```

#### ⚖️ **8. `match-case` (Pattern Matching)**
- Like a switch-case (introduced in Python 3.10):
```python
def rishta(income):
    match income:
        case 0: return "Poor"
        case 100000: return "Rich"
```

---

## 🛠️ Bonus Tools for Python

### 🧪 **pytest - Python Testing Made Simple**
- A lightweight framework to write **unit tests**.

**Why?** → Makes sure your code works as expected.

**How?**
```bash
pip install pytest
```

**Example:**
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run it:
```bash
pytest
```

---

### 🔍 **mypy - Static Type Checking**
- Checks if your variable types match what you’ve declared (helps catch bugs early).

**Install:**
```bash
pip install mypy
```

**Example:**
```python
def greet(name: str) -> str:
    return "Hello " + name
```

Then run:
```bash
mypy your_file.py
```

✅ If types match, all is good. ❌ If not, mypy will show where you went wrong.

---

## 🚀 Pro Tips to Memorize Everything:
- 🔁 Practice writing `match-case`, string interning, and binary reading.
- 🧠 Use `id()` and `is` to explore how memory works.
- 📦 Explore `pytest` and `mypy` in small projects.
- 💡 Make flashcards of key terms: `complex`, `bin()`, `intern()`, `id()`.

