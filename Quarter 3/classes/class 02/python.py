# Python Basics - Class 02

# Printing a simple message
print("hello Okasha")

# String Methods Demonstrations
name = "Okasha Nadeem"
print(name.upper())       # Convert to uppercase
print(name.lower())       # Convert to lowercase
print(name.capitalize())  # Capitalize the first letter
print(name.title())       # Capitalize the first letter of each word
print(len(name))          # Get the length of the string

# Stripping whitespaces
print(name.strip())   # Remove leading and trailing spaces
print(name.lstrip())  # Remove leading spaces
print(name.rstrip())  # Remove trailing spaces

# Replacing values in a string
value = "Okasha"
print(value.replace("Okasha", "Nadeem"))  # Replace full string
print(value.replace("a", "A"))             # Replace all 'a' with 'A'
print(value.replace("a", "A", 1))         # Replace only the first 'a'

# Finding index of a character
value1 = "Name"
print(value1.index("a"))  # Returns index of first occurrence of 'a'
print(value1.find("a"))   # Similar to index but does not raise an error if not found

# Difference between find() and index()
print(value1.find("i"))   # Returns -1 since 'i' is not found
# print(value1.index("i")) # Would raise an error since 'i' is not found

# Checking string start and end
value2 = "Ramzan Mubarak"
print(value2.startswith("Ramzan"))   # True
print(value2.startswith("Mubarak"))  # False
print(value2.endswith("Mubarak"))    # True
print(value2.endswith("Ramzan"))     # False

# Conditional check with startswith
if value2.startswith("Ramzan"):
    print("Ramzan Mubarak")
else:
    print("Eid Mubarak")

# Splitting a string into a list
value3 = "jan,feb,march,april,may,june,july"
print(value3.split(","))

# Demonstrating list methods
mylist = ['jan', 'feb', 'march', 'april']
print(mylist.append("july"))    # Append an element (returns None, modifies list in-place)
print(mylist.insert(0, "dec"))  # Insert an element at a specific index

# Removing elements
removed_item = mylist.pop()  # Remove the last item and return it
print(removed_item)

# Extending lists
mylist1 = ['jan', 'feb', 'march', 'april']
mylist2 = ['may', 'jun', 'july', 'august']
mylist1.extend(mylist2)  # Extend list1 with elements of list2
print(mylist1)

# Concatenating lists
list3 = mylist1 + mylist2
print(list3)

# Sorting a list
mylist3 = [1, 5, 3, 6, 2, 4]
mylist3.sort()  # Sort in ascending order
print("sort ascending: ", mylist3)

mylist3.sort(reverse=True)  # Sort in descending order
print("sort descending: ", mylist3)

mylist3.reverse()  # Reverse the order of elements
print("reversed method: ", mylist3)

mylist3.remove(5)  # Remove the element 5 from the list
print("removed Item: ", mylist3)

# Copying lists
mylist3_copy = mylist3.copy()
print("Copy List: ", mylist3_copy)

# Slicing lists
mylist3_copy2 = mylist3[0:3]  # Get first 3 elements
print(mylist3_copy2)

mylist3_copy3 = mylist3[0:3:2]  # Get elements with a step of 2
print(mylist3_copy3)

# Dictionary methods
student = {
    "Name": "Ali",
    "Age": 15
}

student.update({"Roll Number": 178})  # Update dictionary with new key-value pair
print("update display: ", student)

print("Pop: ", student.pop("Name"))  # Remove key "Name" and return its value
print("Pop Item: ", student.popitem())  # Remove and return the last key-value pair

print("Keys: ", student.keys())  # Get all keys
print("values: ", student.values())  # Get all values
print("items: ", student.items())  # Get all key-value pairs

# Iterating through dictionary items
for k, value in student.items():
    print(f"item key: {k} and value: {value}")

for tup in student.items():
    print("tuple: ", tup)

# Unpacking dictionary items
for tup in student.items():
    a, b = tup
    print("a:", a)
    print("b:", b)

# Homework: Demonstrating del
student = {"Name": "Ali", "Age": 15, "Roll Number": 178}
del student["Age"]  # Delete specific key
print("Dictionary after deleting 'Age':", student)

del student  # Delete the entire dictionary (will cause error if accessed later)
