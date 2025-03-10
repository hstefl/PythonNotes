"""
The pickle module is used for serializing objects as a single byte stream. Both serializing and deserializing parties
must abide by the order of all the elements placed into a file or database, or sent via a network.

There is another handy module, called shelve, that is built on top of pickle, and implements a serialization
dictionary where objects are pickled and associated with a key. The keys must be ordinary strings, because the
underlying database (dbm) requires strings.

Python puts the changes in a buffer which is periodically flushed to the disk.
To enforce an immediate flush, call the sync() method on your shelve object;
"""

import shelve

shelve_name = 'first_shelve.shlv'

# flag - Value	Meaning
# 'r'	Open existing database for reading only
# 'w'	Open existing database for reading and writing
# 'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
# 'n'	Always create a new, empty database, open for reading and writing
my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()
