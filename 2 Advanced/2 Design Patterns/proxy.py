"""
The Proxy pattern is a structural design pattern that acts as an intermediary for another object. It is used to control access, add functionality, or defer the full cost of object initialization.

When to Use the Proxy Pattern
 * Lazy initialization (Virtual Proxy): Creating resource-intensive objects only when needed.
 * Access control (Protection Proxy): Controlling permissions to access the real object.
 * Remote proxies: Representing an object that exists in a different address space.
 * Logging and monitoring (Logging Proxy): Recording actions performed on the object.
 * Caching (Smart Proxy): Storing temporary results for expensive operations.
"""

# Example 1: Virtual Proxy (Lazy Initialization)
class RealImage:
    """Expensive object to load"""
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")


class ProxyImage:
    """Proxy that controls access to RealImage"""
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None  # Lazy initialization

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)  # Initialize only when needed
        self.real_image.display()


# Usage
image1 = ProxyImage("photo1.jpg")
image2 = ProxyImage("photo2.jpg")

# No image is loaded yet
image1.display()  # Loading occurs here
image1.display()  # No loading, just displaying

# -------------------------------------------------------------

# Example 2: Protection Proxy
class RealBankAccount:
    """Represents a bank account"""
    def __init__(self, owner):
        self.owner = owner
        self.balance = 1000  # Default balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds!")


class BankAccountProxy:
    """Proxy that restricts access based on user role"""
    def __init__(self, real_account, user_role):
        self.real_account = real_account
        self.user_role = user_role

    def withdraw(self, amount):
        if self.user_role == "owner":
            self.real_account.withdraw(amount)
        else:
            print("Access denied! Only the account owner can withdraw funds.")


# Usage
account = RealBankAccount("John")
proxy = BankAccountProxy(account, "guest")

proxy.withdraw(500)  # Access denied
proxy = BankAccountProxy(account, "owner")
proxy.withdraw(500)  # Withdrawal successful


# ------------------------------------------------------------------------------------

# Example 3: Proxy in Python Standard Library
from functools import lru_cache
import time

class ExpensiveCalculator:
    @lru_cache(maxsize=2)  # Proxy: caching expensive computations
    def compute(self, num):
        print(f"Computing {num}...")
        time.sleep(2)  # Simulating a heavy computation
        return num * num


# Usage
calculator = ExpensiveCalculator()
print(calculator.compute(5))  # Takes 2 seconds
print(calculator.compute(5))  # Returns instantly from cache
