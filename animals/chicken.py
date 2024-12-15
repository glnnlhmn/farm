# Inside animals/chicken.py


class Chicken:
    def __init__(self):
        self.name = "Chicken"

    @staticmethod
    def sound():
        return "Cluck cluck!"

    def interact_with_cow(self):
        from .cow import Cow

        _cow = Cow()
        return f"{self.name} says hi to {_cow.name} and makes a sound: {self.sound()}"

    def interact_with_pig(self):
        from .pig import Pig

        _pig = Pig()
        return f"{self.name} says hi to {_pig.name} and makes a sound: {self.sound()}"

    def interact_with_others(self, cow, pig):
        return f"{self.name} says hi to {cow.name} and {pig.name} and makes a sound: {self.sound()}"