# Inside animals/pig.py


class Pig:
    def __init__(self):
        self.name = "Pig"

    @staticmethod
    def sound():
        return "Oink!"

    def interact_with_chicken(self):
        from .chicken import Chicken

        _chicken = Chicken()
        return f"{self.name} says hi to {_chicken.name} and makes a sound: {self.sound()}"

    def interact_with_cow(self):
        from .cow import Cow

        _cow = Cow()
        return f"{self.name} says hi to {_cow.name} and makes a sound: {self.sound()}"

    def interact_with_others(self, chicken, cow):
        return f"{self.name} says hi to {chicken.name} and {cow.name} and makes a sound: {self.sound()}"