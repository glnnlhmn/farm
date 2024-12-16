# tests/test_farmAnimal.py

import pytest
from farmAnimal import FarmAnimal, AnimalType


def test_chicken_sound():
    chicken = FarmAnimal(AnimalType.CHICKEN)
    assert chicken.sound() == "Cluck"


def test_pig_sound():
    pig = FarmAnimal(AnimalType.PIG)
    assert pig.sound() == "Oink"


def test_cow_sound():
    cow = FarmAnimal(AnimalType.COW)
    assert cow.sound() == "Moo"


def test_interaction_one_animal(expected_interaction_one_animal):
    pig = FarmAnimal(AnimalType.PIG)
    chicken = FarmAnimal(AnimalType.CHICKEN)
    cow = FarmAnimal(AnimalType.COW)

    assert pig.interact_with(chicken) == expected_interaction_one_animal["pig_chicken"]
    assert pig.interact_with(cow) == expected_interaction_one_animal["pig_cow"]
    assert chicken.interact_with(pig) == expected_interaction_one_animal["chicken_pig"]
    assert chicken.interact_with(cow) == expected_interaction_one_animal["chicken_cow"]
    assert cow.interact_with(pig) == expected_interaction_one_animal["cow_pig"]
    assert cow.interact_with(chicken) == expected_interaction_one_animal["cow_chicken"]


def test_interaction_two_animals(expected_interaction_two_animals):
    pig = FarmAnimal(AnimalType.PIG)
    chicken = FarmAnimal(AnimalType.CHICKEN)
    cow = FarmAnimal(AnimalType.COW)

    assert pig.interact_with(chicken, cow) == expected_interaction_two_animals["pig_chicken_cow"]
    assert pig.interact_with(cow, chicken) == expected_interaction_two_animals["pig_cow_chicken"]
    assert chicken.interact_with(pig, cow) == expected_interaction_two_animals["chicken_pig_cow"]
    assert chicken.interact_with(cow, pig) == expected_interaction_two_animals["chicken_cow_pig"]
    assert cow.interact_with(pig, chicken) == expected_interaction_two_animals["cow_pig_chicken"]
    assert cow.interact_with(chicken, pig) == expected_interaction_two_animals["cow_chicken_pig"]


def test_invalid_animal():
    with pytest.raises(ValueError) as excinfo:
        FarmAnimal("Dragon")
    assert str(excinfo.value) == "Invalid animal type: Dragon"