"""
Python allows you to control access to attributes with the built-in property()
function and corresponding decorator @property.

This decorator plays a very important role:
  * it designates a method which will be called automatically when another object
    wants to read the encapsulated attribute value;
  * the name of the designated method will be used as the name of the instance attribute
    corresponding to the encapsulated attribute;
  * it should be defined before the method responsible for setting the value of the
  encapsulated attribute, and before the method responsible for deleting the encapsulated attribute.
"""

class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property # getter
    def level(self):
        return self.__level

    @level.setter # setter - after getter definition
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter # deleter - after getter definition
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None
