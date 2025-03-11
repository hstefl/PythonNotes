"""
Generics allow you to write flexible, reusable, and type-safe code by using type variables instead of specific types.
This helps in writing functions, classes, and data structures that can work with multiple types
while maintaining type safety.

The ways/tools how to approach generics:

Scenario	                            Best Choice	                Why?
-------------------------------------------------------------------------------------------------
General generics (functions/classes)	TypeVar (Python 3.5+) ✅     Ensures type consistency
Fluent interfaces (self return)	        Self (Python 3.11+) ✅       Cleaner than TypeVar
Multiple unknown-length generics        TypeVarTuple (3.12+) ✅      Handles variadic generics
Function wrappers (decorators)	        ParamSpec (3.10+) ✅	        Captures argument types properly
Repeating complex types	                TypeAlias (3.10+) ✅	        Improves readability

Use TypeVar as a default for generics, but switch to newer alternatives if they make your code more readable, concise, and efficient.
"""

# 1. Generics functions
from typing import TypeVar

T = TypeVar("T")  # A generic type variable

def identity(value: T) -> T:
    return value

print(identity(42))       # ✅ int → int
print(identity("hello"))  # ✅ str → str

# ------------------------------------------

# 2. Generics classes
from typing import Generic

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

box_int = Box(100)          # Works with int
box_str = Box("Python")     # Works with str

print(box_int.get_value())  # 100
print(box_str.get_value())  # "Python"

# ------------------------------------------

# 3. Self for Class Methods
from typing import Self

class Fluent:
    def action(self) -> Self:
        print("Action performed!")
        return self  # Self refers to the instance type

obj = Fluent().action()  # Works and keeps type safety

# ------------------------------------------

# 4. TypeAlias for Named Type Hints
from typing import TypeAlias

Vector: TypeAlias = list[float]  # Instead of `List[float]`

def scale(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]

print(scale([1.0, 2.0, 3.0], 2))  # ✅ [2.0, 4.0, 6.0]

# ------------------------------------------

# 5. TypeVarTuple & Unpack for Variadic Generics
from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple("Ts")  # Accepts multiple types

def process(*values: Unpack[Ts]) -> tuple[Unpack[Ts]]:
    return values

result = process(1, "hello", 3.14)  # ✅ (1, "hello", 3.14)
print(result)

# ------------------------------------------

# 6. ParamSpec for Generic Functions with Arbitrary Arguments
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # Captures arbitrary parameters
R = TypeVar("R")    # Captures return type

def decorator(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("Before function call")
        return func(*args, **kwargs)  # Keeps argument structure
    return wrapper

@decorator
def greet(name: str, age: int) -> str:
    return f"Hello, {name}, you are {age}!"

print(greet("Alice", 30))  # ✅ Keeps (name: str, age: int)