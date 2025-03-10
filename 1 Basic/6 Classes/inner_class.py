"""
NOTE: Static classes do not exist in python, inner do.
"""

class OuterClass:
    class InnerClass:
        innerClassField: str = "inner class field"

        def __init__(self, field1):
            self.innerClassField = field1

    def __init__(self, field1):
        self.innerClass = self.InnerClass(field1)


def main() -> None:
    instance_of_inner_class = OuterClass.InnerClass("test")
    print(instance_of_inner_class.innerClassField)

    instance_of_outer_class = OuterClass("test")
    print(instance_of_outer_class.InnerClass.innerClassField)


if __name__ == "__main__":
    main()
