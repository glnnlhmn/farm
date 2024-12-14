# Inside animals/cow.py

from .chicken import Chicken
from .pig import Pig

class Cow:
    def __init__(self):
        self.name = "Cow"

    def moo(self):
        return "Moo!"

    def interact_with_chicken(self):
        chicken = Chicken()
        return f"{self.name} says hi to {chicken.name} and makes a sound: {self.moo()}"

    def interact_with_pig(self):
        pig = Pig()
        return f"{self.name} says hi to {pig.name} and makes a sound: {self.moo()}"

    def interact_with_others(self, chicken, pig):
        return f"{self.name} says hi to {chicken.name} and {pig.name} and makes a sound: {self.moo()}"

if __name__ == "__main__":
    cow = Cow()
    chicken = Chicken()
    pig = Pig()
    print(cow.interact_with_chicken())
    print(cow.interact_with_pig())
    print(cow.interact_with_others(chicken, pig))