from datetime import datetime

"""
Example 1 - decorator as function - function is decorated

Theory:

def decorator():
  ...

def fnc():
   ....
   

decorated = decorator(fnc)
decorated()     

"""


def dec_ts(fnc):
    def c(*args, **kwargs):
        print(f"Starting: {datetime.now()}")
        res = fnc(*args, **kwargs)
        print(f'Result is {res}')
        print(f"Finishing: {datetime.now()}")
        return res

    return c


@dec_ts
def add2num1(a, b):
    return a + b


@dec_ts
def mul2num1(a, b):
    return a * b


print(add2num1(1, 5))
print(mul2num1(1, 5))

"""
Example 2 - decorator with arguments - functions
"""


def dec_ts2(param1, param2):  # arguments of wrapper
    def outer_wrapper(fnc):
        def wrapper(*args, **kwargs):  # arguments of decorated method
            print(f'Before: {param1}, {param2}')
            res = fnc(*args, **kwargs)
            print(f'After: {param1}, {param2}')
            return res

        return wrapper

    return outer_wrapper


@dec_ts2(param1='value1', param2='value2')
def add2num2(a, b):
    return a + b


@dec_ts2(param1='value3', param2='value4')
def mul2num2(a, b):
    return a * b


print(add2num2(1, 5))
print(mul2num2(1, 5))

"""
Example 3 - decorator - class
"""


class DecoClass:
    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):  # arg of decorated method
        print(f'Before')
        res = self.fnc(*args, **kwargs)
        print(f'After')
        return res


@DecoClass
def add2num3(a, b):
    return a + b


@DecoClass
def mul2num3(a, b):
    return a * b


print(add2num3(1, 5))
print(mul2num3(1, 5))

"""
Example 4 - decorator with args - class

Theory:
def decorator(A):
  ...

class MyClass:
  pass
  
  
MyClass = decorator(MyClass)  

"""


class DecoClass:
    def __init__(self, param1):  # args of decorator
        self.param1 = param1

    def __call__(self, fnc):
        def wrapper(*args, **kwargs):  # args of decorated method
            print(f'Before')
            res = fnc(*args, **kwargs)
            print(f'After')
            return res

        return wrapper


@DecoClass(param1='val1')
def add2num3(a, b):
    return a + b


@DecoClass(param1='val2')
def mul2num3(a, b):
    return a * b


print(add2num3(1, 5))
print(mul2num3(1, 5))

"""
Example 5 - decorator of class
"""

print('Example 5 - decorator of class')
def decorator5(cls):
    cls.__getattribute__orig = cls.__getattribute__

    def wrapper(self, attribute_name):
        if attribute_name == 'observe_me':
            print('accessed')
        return cls.__getattribute__orig(self, attribute_name)

    cls.__getattribute__ = wrapper
    return cls


@decorator5
class ToDecorClass:

    def __init__(self):
        self.observe_me = 'init'


obj = ToDecorClass()
print(obj.observe_me)
# print(obj.observe_me)
