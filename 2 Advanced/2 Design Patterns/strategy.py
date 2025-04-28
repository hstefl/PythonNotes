"""
The Strategy design pattern is a behavioral pattern that enables selecting an algorithm's behavior at runtime.
Instead of implementing a single algorithm directly, code receives run-time instructions specifying which
of a family of algorithms to use.

Concept
It defines a family of algorithms, encapsulates each one, and makes them interchangeable.
This pattern lets the algorithm vary independently from clients that use it.

Structure
 * Context: Uses a Strategy object.
 * Strategy: Common interface for all supported algorithms.
 * Concrete Strategies: Implementations of the strategy interface.

When to Use Strategy
 * You need different variants of an algorithm.
 * You want to avoid large if-else or switch statements.
 * You want to isolate algorithm logic and make it interchangeable.

Usage in Python Standard Library
---------------------------------
A classic example is the key parameter in sorting functions like sorted() or list.sort(),
which accepts a strategy for extracting comparison keys:
    ```
    data = ['apple', 'banana', 'cherry']
    sorted(data, key=len)  # Strategy: sort by length
    ```
Here, key=len is a strategy for sorting – different functions (like str.lower, lambda x: x[-1], etc.)
can be passed to modify the sorting behavior.
"""

from abc import ABC, abstractmethod


# Strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


# Concrete Strategies
class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        return sorted(data)  # Simplified for example


class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print("Sorting using quick sort")
        return sorted(data)  # Simplified for example


# Context
class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)


# Usage
data = [5, 3, 8, 1]
context = SortContext(BubbleSortStrategy())
print(context.sort(data))

context.set_strategy(QuickSortStrategy())
print(context.sort(data))
