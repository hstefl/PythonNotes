# Context managers
# Tool for allocating ane releasing resources precisely when it is needed.
#
# Using with Statement
# The with statement is used to wrap the execution of a block of code with methods defined by a context manager.
# This ensures that resources are properly managed, such as opening and closing files, acquiring and releasing locks,
# or setting up and tearing down database connections.
# Example
# `````````````````````````````````````
#  with open('file,txt', 'w') as file
#    file.write("Hello!")
# `````````````````````````````````````
# In this example, file is automatically closed when the block inside the with statement is exited,
# even if an exception is raised.
#
# Implementation
# Class or using generator with contextlib module.

from contextlib import contextmanager


# I. Example with class 1/2
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type:
            print("Exception occurred")
        return True


# II. Example with context manager 1/2
@contextmanager
def my_context_manager():
    print("Entering the context")

    try:
        print("In context - start")
        yield  # this makes this method generator
               # This marks the point where the body of the with statement is executed.
        print("In context - no exception occurred")
    except Exception as e:
        print(f"Exception occurred {e}")
    finally:
        print("Exiting context")


def main() -> None:
    # I. Example with class 2/2
    with MyContextManager() as manager:
        print("Within the context")
        raise ValueError  # simulating exception

    print("------------------")

    # II. Example with context manager 2/2
    with my_context_manager() as manager:
        print("Within the context 1/2")
        print("Within the context 2/2")
        # raise ValueError  # simulating exception


if __name__ == "__main__":
    main()
