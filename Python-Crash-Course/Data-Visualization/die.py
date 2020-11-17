from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides = 6):
        """Assume a six-side die."""
        self.num_sides = num_sides

    def roll(self):
        """return a random number between 1 and number of sides."""
        return randint(1, self.num_sides)