# Exploring Set and Tuple Methods

# Set Methods
my_set = {1, 2, 3, 4, 5}

# add() - Adds an element to the set
my_set.add(6)
print("After add:", my_set)

# remove() - Removes an element (Raises KeyError if not found)
my_set.remove(3)
print("After remove:", my_set)

# discard() - Removes an element (No error if not found)
my_set.discard(10)  # No error
print("After discard:", my_set)

# pop() - Removes and returns a random element
removed_item = my_set.pop()
print("Popped item:", removed_item, "Updated set:", my_set)

# clear() - Removes all elements
my_set.clear()
print("After clear:", my_set)

# union() - Returns a new set with elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))

# intersection() - Returns common elements
print("Intersection:", set1.intersection(set2))

# difference() - Returns elements in set1 but not in set2
print("Difference:", set1.difference(set2))

# symmetric_difference() - Returns elements in either set, but not both
print("Symmetric Difference:", set1.symmetric_difference(set2))


# Tuple Methods
my_tuple = (10, 20, 30, 40, 10)

# count() - Counts occurrences of a value
print("Count of 10:", my_tuple.count(10))

# index() - Returns the index of the first occurrence
print("Index of 30:", my_tuple.index(30))

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked Values:", a, b, c, d, e)

# Converting tuple to list (since tuples are immutable)
my_list = list(my_tuple)
my_list.append(50)
my_tuple = tuple(my_list)
print("Modified Tuple:", my_tuple)

