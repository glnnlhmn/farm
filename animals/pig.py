
# Inside animals/pig.py

from .chicken import Chicken
from .cow import Cow

class Pig:
    def __init__(self):
        self.name = "Pig"

    def oink(self):
        return "Oink!"

    def interact_with_chicken(self):
        chicken = Chicken()
        return f"{self.name} says hi to {chicken.name} and makes a sound: {self.oink()}"

    def interact_with_cow(self):
        cow = Cow()
        return f"{self.name} says hi to {cow.name} and makes a sound: {self.oink()}"

    def interact_with_others(self, chicken, cow):
        return f"{self.name} says hi to {chicken.name} and {cow.name} and makes a sound: {self.oink()}"

if __name__ == "__main__":
    pig = Pig()
    chicken = Chicken()
    cow = Cow()
    print(pig.interact_with_chicken())
    print(pig.interact_with_cow())
    print(pig.interact_with_others(chicken, cow))