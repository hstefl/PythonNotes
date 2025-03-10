from abc import abstractmethod, ABC



# Abstract class with one abstract method
class Base(ABC):
    @abstractmethod
    def implement_me(self):
        raise NotImplementedError


class A(Base):
    classAttrib: str = "HI"

    def __init__(self, attrib1: str, attrib2: str):
        self.__objAttrib1 = attrib1
        self._objAttrib2 = attrib2

    def __str__(self):
        return f"{self.__objAttrib1} {self._objAttrib2}"

    def hello(self):
        raise NotImplementedError("Class is not implemented")

    def implement_me(self):
        pass

    @classmethod
    def class_method(cls):
        print("class method")
        print(cls.classAttrib)

    @staticmethod
    def static_method():
        print("static method")


class B(A):
    def __init__(self, attrib3: str, attrib1: str, attrib2: str):
        super().__init__(attrib1, attrib2)
        self.objAttrib3 = attrib3

    def hello(self):
        print("[B] Hello")

    def __str__(self):
        return f"{super().__str__()} {self.objAttrib3}"


def main() -> None:
    a = A("Hello", "World!")
    print(a.classAttrib)
    # print(a._objAttrib2) # it let compile but IDE warns
    print(a.__str__())
    # print(a.__objAttrib1)  # private
    # print(a.__getattribute__("__objAttrib1")) # private

    b = B("a", "b", "c")
    print(b.__str__())

    print(B.mro())


if __name__ == "__main__":
    main()
