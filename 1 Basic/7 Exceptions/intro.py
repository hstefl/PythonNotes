# Exceptions in Python
# are events that occur during the execution of a program that disrupt the normal flow of instructions.
# They are a critical part of error handling and debugging.

# Exceptions are handled using try, except, else, and finally blocks.

# if nothing happens to take care of the raised exception, the program will be forcibly terminated,
# and you will see an error message sent to the console by Python;

# Exception Hierarchy
# All built-in exceptions are derived from the BaseException class, which is the base class for all exceptions.
# The main hierarchy is as follows:

# BaseException
#     Exception
#         ArithmeticError
#             ZeroDivisionError
#         AttributeError
#         EOFError
#         ImportError
#         IndexError
#         KeyError
#         MemoryError
#         NameError
#         OSError
#             FileNotFoundError
#             PermissionError
#         TypeError
#         ValueError

def main() -> None:
    try:
        10 / 0
    except ZeroDivisionError:
        print("Zero division !")
    else:
        print('This will never happen since this is executed in case of no exception.')
    finally:
        print("Deallocate any resources.")


    try:
        import abcdefghijk

    except ImportError as e:
        print(e.args) # exceptions arguments
        print(e.name) # import error specific arg
        print(e.path) # same as above


if __name__ == "__main__":
    main()
