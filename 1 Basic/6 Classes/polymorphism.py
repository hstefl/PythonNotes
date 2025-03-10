# Polymorphism
#  is a fundamental concept in object-oriented programming (OOP) that allows objects of different
# classes to be treated as objects of a common superclass. It enables methods to do different things based on the
# object it is acting upon, even if they share the same name. Polymorphism provides flexibility and integration of
# new classes with minimal changes to the existing code.

# I. Compile-time Polymorphism (Method Overloading):
# Python does not support method overloading in the same way that languages like Java or C++ do. In Python,
# you can define multiple methods with the same name, but the last defined method will overwrite the previous ones.

class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


m = Math()
# print(m.add(2, 3))  # Error: Python will only recognize the second method definition
print(m.add(2, 3, 4))  # Output: 9


# II. Run-time Polymorphism (Method Overriding):
# This type of polymorphism occurs when a subclass provides a specific implementation of a method that is already
# defined in its superclass. This allows the subclass to modify or extend the behavior of that method.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!

# Polymorphism with Duck Typing
# Duck typing in Python is a concept where the type or class of an object is less important than the methods it defines.
# If an object implements the required methods, it can be used in place of another object. This is a form of
# polymorphism where the actual type of the object is not checked.


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Person:
    def speak(self):
        return "Hello!"


def make_it_speak(entity):
    print(entity.speak())


dog = Dog()
cat = Cat()
person = Person()

make_it_speak(dog)    # Output: Woof!
make_it_speak(cat)    # Output: Meow!
make_it_speak(person) # Output: Hello!