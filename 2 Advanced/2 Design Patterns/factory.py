"""
The Factory Pattern is a creational design pattern
that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects
that will be created. It helps encapsulate object creation logic, making code more scalable and maintainable.

The Factory Pattern is a powerful design pattern that is useful when:
  * The exact type of object to be created isn't known until runtime.
  * We need to manage different object creation logic in a central place.
  * There’s a need to reduce tight coupling between object creation and usage.

Usage of Singleton in Python Standard Library
---------------------------------------------
The multiprocessing.Process class internally uses a factory pattern to create new process instances.
```
from multiprocessing import Process

def print_hello():
    print("Hello from process!")

# Factory method is used to create a new Process instance
p = Process(target=print_hello)
p.start()
p.join()
```
"""

from abc import ABC, abstractmethod

# Step 1: Create an abstract class/interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Step 2: Create concrete implementations
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Step 3: Implement the Factory Class
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Step 4: Usage
if __name__ == "__main__":
    animal = AnimalFactory.get_animal("dog")
    print(animal.speak())  # Output: Woof!

    animal = AnimalFactory.get_animal("cat")
    print(animal.speak())  # Output: Meow!
