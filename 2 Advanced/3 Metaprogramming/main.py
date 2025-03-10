"""
Metaprogramming is a programming technique in which computer programs have the ability to modify their own
or other programs’ codes.

Metaclass is a class whose instances are classes.

The functionality of the metaclass partly coincides with that of class decorators,
but metaclasses act in a different way than decorators:
  * Decorators bind the names of decorated functions or classes to new callable objects.
    Class decorators are applied when classes are instantiated;
  * Metaclasses redirect class instantiations to dedicated logic, contained in metaclasses.
    Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.


In Python's approach, everything is an object, and every object has some type associated with it.
To get the type of any object, make use of the type() function.

metaclasses are used to create classes;
classes are used to create objects;
the type of the metaclass type is type – no, that is not a typo.

type is a class that generates classes defined by a programmer;
metaclasses are subclasses of the type class.


"""


"""
Attributes of metaclasses
"""
class Dog:
    pass

dog = Dog()
print('"dog" is an object of class named:', Dog.__name__)
print()
print('class "Dog" is an instance of:', Dog.__class__)
print('instance "dog" is an instance of:', dog.__class__)
print()
print('class "Dog" is  ', Dog.__bases__)
print()
print('class "Dog" attributes:', Dog.__dict__)
print('object "dog" attributes:', dog.__dict__)


"""
The same information stored in __class__could be retrieved by calling a type() function with one argument:
"""
for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))


"""
When the type() function is called with three arguments, then it dynamically creates a new class. 
    1. Argument specifies the class name; this value becomes the __name__ attribute of the class;
    2. Argument specifies a tuple of the base classes from which the newly created class is inherited; 
       this argument becomes the __bases__ attribute of the class;
    3. Argument specifies a dictionary containing method definitions and variables for the class body; 
       the elements of this argument become the __dict__ attribute of the class and state the class namespace.
       

After the class instruction has been identified and the class body has been executed, the class = type(, , ) code is executed;
the type is responsible for calling the __call__ method upon class instance creation; this method calls two other methods:
    __new__(), responsible for creating the class instance in the computer memory; this method is run before __init__();
    __init__(), responsible for object initialization.       
"""
def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()

"""
Custom metaclass
"""
print()
print("Custom metaclass")

# method to add
def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')

class MyMeta(type):
    def __new__(msc, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings # add method
        obj = super().__new__(msc, name, bases, dictionary)
        obj.cust_attribute = 'default value of custom attribute' # this will "class"! attribute
        return obj


class MyClass(metaclass=MyMeta):
    pass

class MyClass2(metaclass=MyMeta):
    def greetings(self):
        print('We are ready to greet you!')

myClass = MyClass()
print(MyClass.__dict__)
print(MyClass.cust_attribute)
print(myClass.__dict__)


myobj1 = MyClass()
myobj1.greetings()
myobj2 = MyClass2()
myobj2.greetings()