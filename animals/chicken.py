# Inside animals/chicken.py

from .cow import Cow
from .pig import Pig

class Chicken:
    def __init__(self):
        self.name = "Chicken"

    def cluck(self):
        return "Cluck cluck!"

    def interact_with_cow(self):
        cow = Cow()
        return f"{self.name} says hi to {cow.name} and makes a sound: {self.cluck()}"

    def interact_with_pig(self):
        pig = Pig()
        return f"{self.name} says hi to {pig.name} and makes a sound: {self.cluck()}"

    def interact_with_others(self, cow, pig):
        return f"{self.name} says hi to {cow.name} and {pig.name} and makes a sound: {self.cluck()}"

if __name__ == "__main__":
    chicken = Chicken()
    cow = Cow()
    pig = Pig()
    print(chicken.interact_with_cow())
    print(chicken.interact_with_pig())
    print(chicken.interact_with_others(cow, pig))