"""
Imagine a situation where you are already handling an exception and your code incidentally triggers an additional
exception. Should your code lose the information about the previous exception? Of course not.
So the information should be available to the code following the erroneous code. This is an example of implicit chaining.

Another case pops up when we knowingly wish to handle an exception and translate it to another type of exception.
Such a situation is typical when you have a good reason for the unifying behavior of one piece of code to act
similarly to another piece of code, like a legacy code. In this situation it would also be nice to keep
the details of the former exception. This is an example of explicit chaining.


This chaining concept introduces two attributes of exception instances:
  * the __context__ attribute, which is inherent for implicitly chained exceptions;
  * the __cause__ attribute, which is inherent for explicitly chained exceptions.

"""


"""
Implicit chaining
"""
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)

print('=============')


"""
Explicit chaining
"""
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))
