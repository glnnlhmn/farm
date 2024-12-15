# Inside animals/cow.py


class Cow:
    def __init__(self):
        self.name = "Cow"

    @staticmethod
    def sound():
        return "Moo!"

    def interact_with_chicken(self):
        from .chicken import Chicken

        _chicken = Chicken()
        return f"{self.name} says hi to {_chicken.name} and makes a sound: {self.sound()}"

    def interact_with_pig(self):
        from .pig import Pig

        _pig = Pig()
        return f"{self.name} says hi to {_pig.name} and makes a sound: {self.sound()}"

    def interact_with_others(self, chicken, pig):
        return f"{self.name} says hi to {chicken.name} and {pig.name} and makes a sound: {self.sound()}"