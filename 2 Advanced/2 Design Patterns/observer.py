"""
Observer Design Pattern
The Observer design pattern is a behavioral design pattern that defines a one-to-many dependency between objects.
When one object (the "subject") changes state, all its dependents (the "observers") are notified and
updated automatically. This is commonly used to implement distributed event-handling systems.

Key Concepts
 * Subject: Maintains a list of observers and provides methods to add, remove, and notify them of state changes.
 * Observer: Defines an interface for objects that should be notified of changes in the subject's state.
 * Concrete Subject: Implements the subject interface and stores state.
 * Concrete Observer: Implements the observer interface and updates its state based on notifications from the subject.

Use Cases of Observer Pattern
 * Event management systems.
 * Real-time data feeds (e.g., stock prices, weather updates).
 * Model-View-Controller (MVC) architecture, where the model notifies the view of changes.

This implementation is flexible, as you can add or remove observers dynamically without changing the subject.
"""
from abc import ABC, abstractmethod


# Subject Interface
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()  # Notify observers whenever temperature changes


# Concrete Observer
class TemperatureDisplay(Observer):
    def update(self, subject):
        if isinstance(subject, WeatherStation):
            print(f"Temperature Display: The temperature is now {subject.temperature}°C")


class AlertSystem(Observer):
    def update(self, subject):
        if isinstance(subject, WeatherStation) and subject.temperature > 30:
            print("Alert System: Temperature is above 30°C! Warning issued.")


# Example Usage
if __name__ == "__main__":
    weather_station = WeatherStation()

    display = TemperatureDisplay()
    alert = AlertSystem()

    weather_station.attach(display)
    weather_station.attach(alert)

    weather_station.temperature = 25
    weather_station.temperature = 35
