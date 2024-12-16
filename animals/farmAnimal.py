"""
farmAnimal.py

This module defines the FarmAnimal class and the AnimalType enum. The FarmAnimal class represents a farm animal with a type and sound,
and provides methods for interacting with other farm animals. The AnimalType enum lists different types of farm animals and their sounds.

Classes:
    AnimalType (Enum): Enum representing different types of farm animals and their sounds.
    FarmAnimal: Class representing a farm animal with a type and sound.

Usage example:
    from farmAnimal import FarmAnimal, AnimalType

    pig = FarmAnimal(AnimalType.PIG)
    chicken = FarmAnimal(AnimalType.CHICKEN)
    cow = FarmAnimal(AnimalType.COW)

    print(pig.interact_with(chicken))
    print(chicken.interact_with(pig, cow))
    print(cow.interact_with(chicken, pig))
"""

import sys
from enum import Enum

# Check for minimum Python version
MIN_VERSION = (3, 9)
if sys.version_info < MIN_VERSION:
    sys.exit(f"Python {MIN_VERSION[0]}.{MIN_VERSION[1]} or higher is required.")


class AnimalType(Enum):
    """Enum representing different types of farm animals and their sounds."""
    CHICKEN = "Cluck"
    PIG = "Oink"
    COW = "Moo"


class FarmAnimal:
    """Class representing a farm animal with a type and sound.

    Attributes:
        type (str): The type of the animal.
        _sound (str): The sound the animal makes.
    """

    def __init__(self, animal_type: AnimalType):
        """
        Initialize a FarmAnimal instance.

        Args:
            animal_type (AnimalType): The type of the animal.

        Raises:
            ValueError: If the animal_type is not a valid AnimalType.
        """
        if not isinstance(animal_type, AnimalType):
            raise ValueError(f"Invalid animal type: {animal_type}")
        self.type: str = animal_type.name.capitalize()
        self._sound: str = animal_type.value

    def interact_with(self, *animals: 'FarmAnimal') -> str:
        """
        Generate a string describing the interaction with other animals.

        Args:
            animals (FarmAnimal): Other farm animals to interact with.

        Returns:
            str: A description of the interaction.
        """
        animal_list: str = self._build_animal_list(self, animals)
        animal_text: str = self._build_text_with_and(animal_list)
        sounds_list: list[str] = self._build_sounds_list(self, animals)
        sounds_text: str = self._build_text_with_and(sounds_list)
        return f"This morning in the barn yard there is {animal_text}. You hear {sounds_text}!"

    def _build_animal_list(self, calling_animal: 'FarmAnimal', animals: list['FarmAnimal']) -> list[str]:
        """
        Build the animal list for the interaction description.

        Args:
            calling_animal (FarmAnimal): The animal calling the interaction.
            animals (list[FarmAnimal]): List of other farm animals.

        Returns:
            list[str]: A list of descriptions of the animals.
        """
        all_animals = [calling_animal] + list(animals)
        return [f"a {animal.type.lower()}" for animal in all_animals]

    def _build_sounds_list(self,  calling_animal: 'FarmAnimal', animals: list['FarmAnimal']) -> list[str]:
        """
        Build the sounds list for the interaction description.

        Args:
            animals (list[FarmAnimal]): List of farm animals.

        Returns:
            list[str]: A list of descriptions of the sounds made by the animals.
        """
        all_animals = [calling_animal] + list(animals)
        return [f"the {animal.type.lower()} {animal.sound().lower()}" for animal in all_animals]


    def _build_text_with_and(self, items: list[str]) -> str:
        """
        Build a text string from a list of items, using commas and 'and' appropriately.

        Args:
            items (list[str]): List of items to join into a string.

        Returns:
            str: A string with items joined by commas and 'and'.
        """
        if not items:
            return ""
        if len(items) == 1:
            return items[0]
        if len(items) == 2:
            return f"{items[0]} and {items[1]}"
        return ', '.join(items[:-1]) + f", and {items[-1]}"

    def sound(self) -> str:
        """
        Get the sound the animal makes.

        Returns:
            str: The sound of the animal.
        """
        return self._sound