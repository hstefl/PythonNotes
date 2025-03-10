"""
The Template Method design pattern defines the skeleton of an algorithm in the superclass
but lets subclasses alter specific steps of the algorithm without changing its structure.

Key Features
 * Defines a template (abstract) method that outlines the algorithm.
 * Allows subclasses to implement specific steps of the algorithm.
 * Reduces code duplication by reusing a common structure.

Example in Python’s Standard Library
------------------------------------
Python’s unittest module uses the Template Method pattern. The unittest.TestCase class provides a run method
that defines the test execution flow while allowing subclasses to define individual tests.
"""


from abc import ABC, abstractmethod

class Beverage(ABC):
    """Abstract class defining the template method for preparing a beverage."""

    def prepare_beverage(self):
        """Template method defining the steps to make a beverage."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        """Step to brew the beverage (to be implemented by subclasses)."""
        pass

    @abstractmethod
    def add_condiments(self):
        """Step to add condiments (to be implemented by subclasses)."""
        pass

class Tea(Beverage):
    """Concrete class implementing tea-specific steps."""

    def brew(self):
        print("Steeping the tea bag")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(Beverage):
    """Concrete class implementing coffee-specific steps."""

    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

# Usage
print("Making Tea:")
tea = Tea()
tea.prepare_beverage()

print("\nMaking Coffee:")
coffee = Coffee()
coffee.prepare_beverage()

