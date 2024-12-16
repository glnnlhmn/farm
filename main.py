# Usage example
from animals.farmAnimal import FarmAnimal, AnimalType

def main():
    pig = FarmAnimal(AnimalType.PIG)
    chicken = FarmAnimal(AnimalType.CHICKEN)
    cow = FarmAnimal(AnimalType.COW)

    print(pig.interact_with(chicken))
    print(chicken.interact_with(pig, cow))
    print(cow.interact_with(chicken, pig))

if __name__ == "__main__":
    main()