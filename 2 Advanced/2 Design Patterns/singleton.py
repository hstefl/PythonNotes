"""
The Singleton pattern is a creational design pattern
that ensures that a class has only one instance and provides a global point of access to that instance.

This is useful when you need a single point of control, such as managing
configurations, logging, caching, or database connections.

Usage of Singleton in Python Standard Library
---------------------------------------------
Singleton is used in many places in the Python standard library, including:

logging module

1. The logging.getLogger() method returns the same instance of the logger throughout the program.
```
import logging

logger1 = logging.getLogger("my_logger")
logger2 = logging.getLogger("my_logger")

print(logger1 is logger2)  # True
```

2. The os.environ dictionary, which holds environment variables, follows a singleton pattern.
threading.Thread instances (for same target)

3. Thread instances referring to the same function behave like a singleton.
functools.lru_cache

4. Used for caching function results, ensuring the same function call with the same arguments returns cached results.
"""


# 1. Using a Class with a Private Instance Variable (Classic Singleton)
# ✅ Pros: Simple and effective
# ❌ Cons: Does not prevent subclassing issues
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Method __new__ is responsible for creating a new instance of a class before it is initialized by __init__.
        It is static (class method).
        It returns the newly created instance, which is then passed to __init__ for initialization.
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# --------------------------------------------------------------------------

# 2. Using a Decorator
# ✅ Pros: Reusable and clean implementation
# ❌ Cons: May not work well with inheritance
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class SingletonDeco:
    pass

# --------------------------------------------------------------------------

# 3. Using a Metaclass
# ✅ Pros: Works well with inheritance
# ❌ Cons: Slightly more complex
class MetaClassSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super.__call__(cls, *args, **kwargs)

        return cls._instances[cls]

class SingletonMeta(metaclass=MetaClassSingleton):
    pass


# --------------------------------------------------------------------------

# 4. Using a module
# Since Python modules are singleton by nature. - When a module is imported, it is loaded into memory once and
# cached in sys.modules. Any subsequent import of that module returns the same instance, which fulfills the
# requirements of the Singleton pattern.
#
# Following code should go to separate module and other modules can import it to use singleton_instance.
"""
# singleton_module.py
class Singleton:
    def __init__(self):
        print("Singleton Instance Created")

singleton_instance = Singleton()
"""




if __name__ == '__main__':
    # 1. Using a Class with a Private Instance Variable (Classic Singleton)
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)

    # 2. Using a decorator
    s3 = SingletonDeco()
    s4 = SingletonDeco()
    print(s3 is s4)

    # 3. Using a Metaclass
    s5 = SingletonMeta()
    s6 = SingletonMeta()
    print(s5 is s6)