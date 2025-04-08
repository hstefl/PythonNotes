"""
The Builder design pattern is a creational pattern that lets you construct complex objects step by step.
It separates the construction of a complex object from its representation, so the same construction process
can create different representations.

Structure
 * Builder – Specifies an abstract interface for creating parts of a Product.
 * ConcreteBuilder – Implements the Builder interface and keeps track of the representation.
 * Director – Constructs an object using the Builder interface.
 * Product – The complex object under construction.

Python doesn’t use the Builder pattern as explicitly as Java or C++ because:
 1. Dynamic Typing & Flexible Constructors
    Python's dynamic nature allows objects to be created and modified more easily at runtime.
    ```
        class Car:
            def __init__(self, wheels=4, engine="V6", sunroof=False):
                self.wheels = wheels
                self.engine = engine
                self.sunroof = sunroof

        car = Car(wheels=6, sunroof=True)  # Custom configuration, no builder needed
    ```

 2. Default Arguments & **kwargs
    Python supports default values and keyword arguments out of the box,
    making step-by-step configuration simple without a separate Builder.
    ```
       def make_email(subject=None, to=None, body=""):
           return {"subject": subject, "to": to, "body": body}

        email = make_email(subject="Hello", body="Hi there!")
    ```

 3. NamedTuples & Data Classes
    With @dataclass (Python 3.7+), you get a flexible and declarative way to define and build objects:
    ```
        from dataclasses import dataclass

        @dataclass
        class Pizza:
            dough: str
            sauce: str
            topping: str = "cheese"

        pizza = Pizza(dough="thin", sauce="tomato")
    ```

 4. Fluent Interfaces Are Easy
 ```
     class FluentEmail:
        def __init__(self):
            self.message = {}

        def to(self, recipient):
            self.message['to'] = recipient
            return self

        def subject(self, text):
            self.message['subject'] = text
            return self

        def body(self, content):
            self.message['body'] = content
            return self

     email = FluentEmail().to("you@example.com").subject("Hi").body("Hello!")
     ```
"""


# Product
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.door = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, and {self.door} door"


# Builder
class HouseBuilder:
    def walls(self) -> House: pass

    def roof(self) -> House: pass

    def door(self) -> House: pass

    def build(self) -> House: pass


# Concrete Builder
class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def walls(self) -> HouseBuilder:
        self.house.walls = "wooden"
        return self

    def roof(self) -> HouseBuilder:
        self.house.roof = "shingle"
        return self

    def door(self) -> HouseBuilder:
        self.house.door = "oak"
        return self

    def build(self) -> House:
        return self.house


# Director
class Director:
    def __init__(self, b: HouseBuilder):
        self._builder = b

    def construct(self):
        self._builder.walls().roof().door()

        return self._builder.build()


# Client Code
builder = WoodenHouseBuilder()
director = Director(builder)
house = director.construct()
print(house)  # House with wooden walls, shingle roof, and oak door
