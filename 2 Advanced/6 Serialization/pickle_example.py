"""
Object serialization is the process of converting an object structure into a stream of bytes to store the
object in a file or database, or to transmit it via a network. This byte stream contains all the information necessary
to reconstruct the object in another Python script.

The following types can be pickled:
    None, booleans;
    integers, floating-point numbers, complex numbers;
    strings, bytes, bytearrays;
    tuples, lists, sets, and dictionaries containing pickleable objects;
    objects, including objects with references to other objects (remember to avoid cycles!)
    references to functions and classes, but not their definitions.


Note that functions (both built-in and user-defined) are pickled by their name reference, not by any value.
This means that only the function name is pickled; neither the function’s code, nor any of
its function attributes, are pickled.
Similarly, classes are pickled by named reference, so the same restrictions in the unpickling environment apply.
Note that none of the class’s code or data are pickled.
This is done on purpose, so you can fix bugs in a class or add methods to the class, and still load objects that were
created with an earlier version of the class.
Hence, your role is to ensure that the environment where the class or function is unpickled is able to import the
class or function definition. In other words, the function or class must be available in the namespace of
your code reading the pickle file.


the pickle module is constantly evolving, so the binary format may differ between different versions of Python.
Pay attention that both serializing and deserializing parties are making use of the same pickle versions;

"""
import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open('multidata.pckl', 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)

with open('multidata.pckl', 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)

"""
Example with using custom driver other then file
"""
a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print('A type of deserialization')