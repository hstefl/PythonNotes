from typing import List, Tuple, Set, Dict, FrozenSet

# Immutable types
# ----------------
i: int = 10 # unbounded - can grow as needed

# Floating-point numbers cannot represent all real numbers exactly due to the finite number of bits used.
# This can lead to rounding errors.
# For example, 0.1 + 0.2 is not exactly 0.3 in floating-point arithmetic.
# To avoid rounding errors, use the decimal module or the fractions module.
# Since float uses hardware-level floating-point arithmetic (IEEE 754), it is usually quite fast.
f: float = 3.14 # 64bit
s: str = "string"

# Python considers the following values as falsy:
#   None
#   False
#   0 (integer or float)
#   Empty sequences and collections: '', [], {}, (), set(), range(0)
#   Empty custom objects implementing __bool__() or __len__() that return False or 0.
# Everything else is truthy, including:
#   Non-zero numbers (e.g., 1, 3.14, -1)
#   Non-empty sequences and collections (e.g., 'hello', [1, 2, 3], {1: 'a'})
b: bool = True

# Tuple
#   Collection which is ordered and immutable
#   build-in data type (besides List, Set, Dictionary)
#   Complexities
#     Time
#       Accessing (t[x]): O(1), because of nature of array
#       Slicing (t[start,end]): O(m), m = number of sliced items
#       Concatenation (t1+t2): O(m+n), m and n are sizes of tuples
#     Space
#       O(n), n is size of tuple
#   Usage
#     + memory optimization aspects (because of nature of immutability and lazy loading)
#     + Fixed memory layout: Because the size is fixed at creation time, tuples can be more memory efficient and
#       faster than lists for lookups and iteration.
#     + Optimized for immutability: Due to immutability, tuples do not require memory reallocation, making them faster
#       to create than lists when a collection of items with a known size is needed.
#   Implementation in Python
#     Struct in C contain
#       pointer to array of Python object
#       current size of tuple
#       allocated memory size
#
# Tuple Operations and Methods in Python
# Operation/Method           | Description                                               | Example
# -----------------------------------------------------------------------------------------------
# Indexing                   | Access individual elements by index                       | t[0]
# Slicing                    | Access a range of elements                                | t[1:3]
# Concatenation (+)          | Concatenate two tuples                                    | (1, 2) + (3, 4)
# Repetition (*)             | Repeat the tuple multiple times                           | (1, 2) * 3
# Membership                 | Check if an element exists in the tuple                   | 2 in t
# Length (len())             | Get the number of elements in the tuple                   | len(t)
# count()                    | Count occurrences of a value                              | t.count(2)
# index()                    | Find the index of the first occurrence of a value         | t.index(2)
# Unpacking                  | Assign elements to variables                              | a, b, c = t
# Iteration                  | Loop over elements                                        | for item in t:
# Immutability               | Cannot modify elements after creation                     | t[0] = 1  # TypeError
# Tuples as Dictionary Keys  | Use tuples as dictionary keys due to immutability         | d[(1, 2)] = "value"
# Nested Tuples              | Tuples can contain other tuples                           | t = (1, (2, 3), 4)
# Comparison                 | Compare tuples element-wise                               | (1, 2) < (1, 3)
# max(), min(), sum()        | Compute maximum, minimum, and sum for numerical tuples     | max(t), min(t), sum(t)
t: Tuple[int, int, int, int] = (10, 11, 12, 13)

# Frozenset complexities
#   Time
#     presence check: O(1) (usually - based by nature of hashing)
#     union, intersection, difference: O(n), n is the size of the smaller frozenset
#   Space
#     O(n), n is size of frozenset
# Usage
#   Scenarios where you need to store a collection of unique, unchangeable elements or
#   use them as keys in dictionaries or elements in other frozensets.
# Implementation in Python
#   Hashtable
fs: FrozenSet[int] = frozenset([20, 21])
by: bytes = b'binary-data'

# Mutable types
# List
#   Collection which is ordered and mutable
#   Time complexity
#     accessing (l[x]): O(1)
#     appending (l.append(value)): O(1)
#     deleting (l.delete(value)): O(n)
#       because of shifting all items after inserted item (new array is possible needed to create)
#     deleting (l.delete(i)): O(1), we know the position
#     insert (l.insert(value): O(n),
#       because of shifting all items after inserted item (new array is possible needed to create)
#     pop (l.pop()): O(1), no shifting is needed
#     concatenation (l1 + l2): O(k), k is the size of l2, it creates new list and copied items there
#   Space complexity
#      O(n), n is number elements in a list
# Usage
#   Scenarios where you need a mutable collection of ordered (as they were added) items and where operations like
#   appending, accessing elements by index, or modifying elements are frequent.
# Implementation in Python
#   Dynamic array
l1: List[int] = [10, 11, 12]
l2: List[int] = list((10, 20, 30)) # Tuple -> List

# Dictionary complexities
#   Time
#     accessing (l[key]): O(1) typically
#     inserting (l[key] = value)): O(1) typically
#     deleting (l.delete(key)): O(1) typically
#   Space
#      O(n), n is number elements in a dictionary
# Usage
#   Scenarios where you need a quick lookpup, insertion and deletion of items.
# Implementation in Python
#   hash table
d: Dict[str, int] = {"a": 1, "b": 2}

# Set complexities
#   Time
#     like in frozenset
#   Space
#     like in frozenset
# Usage
#   Unique elements
#   fast average-time complexity for membership tests, insertions, deletions, and set operations.
# Implementation in Python
#   Hash table
se: Set[int] = {10, 11, 12}


def main() -> None:
    # Tuple comprehensions
    newT = (i*i for i in t) # this provides generator expression
    first_element:int = t[0]
    print(tuple(newT))

    # List comprehensions
    squares = [i * i for i in l1]
    print(squares)
    squares = [i * i for i in l1 if i % 2 == 0]
    print(squares)
    matrix = [[f"{j},{i}" for i in range(3)] for j in range(3)]
    print(matrix)

    # Set comprehensions
    triples = {i*i for i in se}
    print(triples)
    triples = {i*i for i in se if i % 2 == 0}
    print(triples)

    # Dictionary comprehensions
    newDict = {k:v for k,v in d.items()}
    print(newDict)
    newDict2 = {k: f"{v} is even" if v%2 == 0 else f"{v} is odd" for k,v in d.items()}
    print(newDict2)


if __name__ == "__main__":
    main()
