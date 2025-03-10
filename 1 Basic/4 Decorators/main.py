# Decorators
# The tool which enable to extend/modify existing methods or functions.
# It is a function which accepts function to modify and return function with modified behaviour.
# This methods contains definition of inner funtion `wrapper()` where the input function is hanlded.
#
# Use cases
# Cross-cutting concerns like logging, controlling of access, instrumentation or caching, ...

# method decorator
def my_decorator(func):
    def wrapper(*args, **kwags) -> bool:
        print("Before!")
        result = bool(func(*args, **kwags))
        print("After!")
        return result

    return wrapper


def another_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before another")
        result = func(*args, **kwargs)
        print("After another")
        return result

    return wrapper


@my_decorator  # shortcut for say_hellos = my_decorator(say_hello)
@another_decorator
def say_hello(name: str) -> bool:
    print(f"Hello {name}!")
    return True


# class decorator
def class_decorator(cls):
    class WrapperClass(cls):
        def new_method(self):
            print("New method")

    return WrapperClass


@class_decorator
class MyClass:
    def original_method(self):
        print("Original method")


def main() -> None:
    say_hello("Jan")
    MyClass().original_method()
    MyClass().new_method()


if __name__ == "__main__":
    main()
