import random
from dataclasses import dataclass


@dataclass
class Dice:
    value: int = random.randrange(1, 7)

    def roll(self):
        self.value = random.randrange(1, 7)
        return self.value
