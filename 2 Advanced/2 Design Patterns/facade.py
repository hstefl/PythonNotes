"""
The Facade pattern is a structural design pattern that provides a simplified interface to a complex
system of classes, libraries, or APIs. It hides the complexity of the underlying system and provides
a higher-level interface that makes it easier to use.

Key Features of Facade Pattern:
  Provides a unified interface to a set of interfaces in a subsystem.
  Reduces dependencies between the client and complex subsystems.
  Improves maintainability by centralizing the interaction logic.

"""

# Subsystems
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"Playing '{movie}'")

    def off(self):
        print("DVD Player is OFF")


class Projector:
    def on(self):
        print("Projector is ON")

    def set_input(self, input_source):
        print(f"Projector input set to {input_source}")

    def off(self):
        print("Projector is OFF")


class Amplifier:
    def on(self):
        print("Amplifier is ON")

    def set_volume(self, level):
        print(f"Setting volume to {level}")

    def off(self):
        print("Amplifier is OFF")


# Facade Class
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, amplifier):
        self.dvd_player = dvd_player
        self.projector = projector
        self.amplifier = amplifier

    def watch_movie(self, movie):
        print("\nPreparing to watch a movie...")
        self.dvd_player.on()
        self.dvd_player.play(movie)
        self.projector.on()
        self.projector.set_input("DVD")
        self.amplifier.on()
        self.amplifier.set_volume(10)
        print("Enjoy your movie!")

    def end_movie(self):
        print("\nShutting down the home theater system...")
        self.dvd_player.off()
        self.projector.off()
        self.amplifier.off()
        print("Home theater system turned off.")


# Client Code
if __name__ == "__main__":
    dvd = DVDPlayer()
    projector = Projector()
    amplifier = Amplifier()

    home_theater = HomeTheaterFacade(dvd, projector, amplifier)
    home_theater.watch_movie("Inception")
    home_theater.end_movie()
