"""
The State pattern is a behavioral design pattern that allows an object to change its behavior when its internal
state changes. The object will appear to change its class. This is particularly useful when an object needs
to behave differently depending on its state, without using large conditional statements.

Structure of the State Pattern
 * Context: Maintains an instance of a concrete state object that defines the current state.
 * State Interface: Defines the behavior associated with a particular state.
 * Concrete States: Implement the behavior associated with the state.

When to Use the State Pattern
 * When an object’s behavior depends on its state.
 * When multiple conditional statements (e.g., if-else or switch) control an object’s behavior.
 * When state transitions need to be managed in a scalable and maintainable way.

"""

from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass

    @abstractmethod
    def eject_coin(self, context):
        pass

    @abstractmethod
    def press_button(self, context):
        pass

    @abstractmethod
    def dispense(self, context):
        pass


# Concrete States
class NoCoinState(State):
    def insert_coin(self, context):
        print("Coin inserted.")
        context.set_state(context.has_coin_state)

    def eject_coin(self, context):
        print("No coin to eject.")

    def press_button(self, context):
        print("Insert a coin first.")

    def dispense(self, context):
        print("No coin inserted. Cannot dispense.")

class HasCoinState(State):
    def insert_coin(self, context):
        print("Coin already inserted.")

    def eject_coin(self, context):
        print("Coin ejected.")
        context.set_state(context.no_coin_state)

    def press_button(self, context):
        print("Button pressed. Dispensing item...")
        context.set_state(context.sold_state)

    def dispense(self, context):
        print("Press button to dispense item.")

class SoldState(State):
    def insert_coin(self, context):
        print("Please wait. Dispensing in progress.")

    def eject_coin(self, context):
        print("Cannot eject. Dispensing in progress.")

    def press_button(self, context):
        print("Already dispensing item.")

    def dispense(self, context):
        print("Item dispensed.")
        context.set_state(context.no_coin_state)


# Context Class (Vending Machine)
class VendingMachine:
    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.sold_state = SoldState()

        self.current_state = self.no_coin_state  # Initial state

    def set_state(self, state):
        self.current_state = state

    def insert_coin(self):
        self.current_state.insert_coin(self)

    def eject_coin(self):
        self.current_state.eject_coin(self)

    def press_button(self):
        self.current_state.press_button(self)
        self.current_state.dispense(self)


# Testing the State Pattern
if __name__ == "__main__":
    machine = VendingMachine()

    machine.insert_coin()
    machine.press_button()

    machine.insert_coin()
    machine.eject_coin()
    machine.press_button()
