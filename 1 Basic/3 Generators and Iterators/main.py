# Generators and Iterators in Python
# They are powerful tools in Python that allow you to iterate over data without loading the entire dataset into memory.
# This is especially useful for large datasets or streams of data.
from typing import List, Generator


# Iterators
# An iterator is an object that implements the iterator protocol,
# which consists of the methods __iter__() and __next__().
class MyIterator():
    def __init__(self, data: List[str]):
        self.data = data
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.i < len(self.data):
            item: str = self.data[self.i]
            self.i += 1
            return item
        else:
            raise StopIteration


# Generators
# They are a simple and powerful tool for creating iterators. They are written like regular functions but use the
# yield statement to return data one piece at a time, suspending and resuming their state between each yield.
#
# Differences Between yield and return
# yield produces a value and pauses the function, saving its state for resumption.
# return exits the function completely.
#
# Advantages of Generators
# Memory Efficiency:
#   Generators do not store the entire sequence in memory. They generate each value on the fly,
#   making them suitable for large datasets.
# Representing Infinite Sequences:
#   Generators can represent infinite sequences, such as streams of data or mathematical sequences,
#   without running out of memory.
# Improved Performance:
#   Generators can provide performance improvements by yielding items as needed, rather than constructing
#   the entire list before use.
# Use Cases for Generators
#   Processing Large Files: Reading a file line-by-line without loading the entire file into memory.
#   Streams of Data: Handling data streams from sensors, network connections, or other continuous data sources.
#   Lazy Evaluation: Delaying computation until the result is needed, which can save resources and improve performance.


def my_generator() -> Generator:
    yield 1
    yield 2
    yield 3


def main() -> None:
    print("Iterator")
    iter1: MyIterator = MyIterator(["a", "b", "c", "d"])
    for item in iter1:
        print(item)

    print("Generator")
    for item in my_generator():
        print(item)

    print("Generator expression")
    items = (i for i in range(4))
    for item in items:
        print(item)


if __name__ == "__main__":
    main()
