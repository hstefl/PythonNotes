"""
The built-in id() function returns the 'identity' of an object. This is an integer which is guaranteed to be unique and
constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in the memory. Don’t treat it as an absolute memory address.
"""

"""
Shallow copies
 -> Problem: only addresses are copied not content of objects there
 Note: copy.copy() makes shallow copy
"""
print('Shallow copy')
print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

"""
Deep copies
"""
print('Deep copy')

import copy

print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)



"""
Deep copy of object.
"""
class Example:
    def __init__(self):
        self.properties = ["112", "997"]
        print("Hello from __init__()")

a_example = Example()
b_example = copy.deepcopy(a_example)
print("Memory chunks:", id(a_example), id(b_example))
print("Same memory chunk?", a_example is b_example)
print()
print("Let's modify the movies list")
b_example.properties.append("911")
print('a_example.properties:', a_example.properties)
print('b_example.properties:', b_example.properties)
