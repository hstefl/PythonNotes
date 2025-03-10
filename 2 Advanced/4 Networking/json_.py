import json

i = json.dumps(100)
print(i)

s = json.dumps('Hello "World"')
print(s)

l = json.dumps([1,True, "False", None, ['a', 'b']])
print(l)

# ---------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_person(w):
    if isinstance(w, Person):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

print(json.dumps(Person('John Doe', 42), default=encode_person))

# -------------------------------------

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(w)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))

