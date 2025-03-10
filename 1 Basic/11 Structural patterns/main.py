data = "strawberry ice cream"

# Literal patterns, wildcards and or patterns
match data:
    case "strawberry ice cream" | "something else":
        print("Enjoy strawberry ice cream2")
    case _:
       print("Enjoy your default value")

# Capture pattern
match data:
    # the choice will be always filled - in case you want to prevent that you have to use full qualified name (like Class.property)
    case choice:
        print(f"Enjoy your {choice}")

l = ["blueberry", "strawberry", "ice cream"]
match l:
    case (choice1, choice2, "ice cream"):
        print(f"Enjoy your choice of ice cream: {choice1}, {choice2}")


# Structural patterns and objects
class Pizza:
    def __init__(self, topping, second_topping = None):
        self.first = topping
        self.second = second_topping

order = Pizza("pepperoni", "mushrooms")
match order:
    case Pizza(first="pepperoni", second="mushrooms"):
        print("Standard pizza")
    case Pizza(first="pineapple"):
        print(":(")

order = Pizza("pepperoni", "mushrooms")
#order = Pizza("pepperoni", "tomato")
match order:
    case Pizza(first="pineapple"):
        print(":(")
    case Pizza(first=first, second="mushrooms"):
        print(f"Standard pizza with {first} and mushrooms")
    # always
    case Pizza(first=first, second=second):
        print(f"Standard pizza with {first} and {second}")
    # case _:
    #     print("Other pizzas")


# __match_args__ -> shortcut for pattern matching (see line swith case)
# __match_args__ uses dataclasses implicitly
class Point:
    __match_args__ = ('x_pos', 'y_pos', 'z_pos')

    def __init__(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z

point = Point(1,2,3)

match point:
    case Point(0,0,0):
        print ("Initial point")
    case Point(_,1,3):
        print("Point (_,1,3)")
    case Point(_,_,_):
        print("Any point")


# Structural patterns and Collections (list, tuples, dict)

t = ("ab", "cd", "ef", "gh")

match t:
    case ("cd", *items,"gh"):
        print(" * ".join(items))
    case ("ef", *items2, "gh"):
        print(" - ".join(items2))
    case ("ab", *items3, "gh"):
        print(" + ".join(items3))

# for maps
# case {'key1': val1, 'key2': val2 } etc
