# Inside main.py

from animals import Chicken, Cow, Pig

def main():
    chicken = Chicken()
    cow = Cow()
    pig = Pig()

    print(chicken.interact_with_cow())
    print(chicken.interact_with_pig())
    print(chicken.interact_with_others(cow, pig))

    print(cow.interact_with_chicken())
    print(cow.interact_with_pig())
    print(cow.interact_with_others(chicken, pig))

    print(pig.interact_with_chicken())
    print(pig.interact_with_cow())
    print(pig.interact_with_others(chicken, cow))

if __name__ == "__main__":
    main()