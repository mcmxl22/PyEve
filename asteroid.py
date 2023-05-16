#!/usr/bin/env python3
import random


class Asteroid:
    """Class representing an asteroid with certain materials."""

    def __init__(self):
        """
        Initialize an Asteroid instance with random materials.
        """
        self.materials = self._generate_materials()

    @staticmethod
    def _generate_materials():
        """
        Generate materials for the asteroid.

        Returns:
            dict: A dictionary with a single key-value pair.
                  The key is the material type, and the value is the amount.
        """
        material_types = ['carbon', 'iron', 'copper', 'gold']
        material_proportions = [0.5, 0.3, 0.15, 0.05]
        material_type = random.choices(material_types, material_proportions)[0]
        material_amount = random.randint(50, 1000)
        return {material_type: material_amount}


class AsteroidBelt:
    """Class representing an asteroid belt."""

    def __init__(self):
        """
        Initialize an AsteroidBelt instance with a random number of asteroids.
        """
        self.asteroids = self._generate_asteroids()

    @staticmethod
    def _generate_asteroids():
        """
        Generate a list of asteroids.

        Returns:
            list: A list of Asteroid objects.
        """
        return [Asteroid() for _ in range(random.randint(2, 4))]

    def select_asteroid(self):
        """
        Prompt the user to select an asteroid to mine.

        Returns:
            Asteroid: The selected Asteroid object.
        """
        self._check_and_regenerate()
        self._display_asteroids()
        return self._user_select_asteroid()

    def _check_and_regenerate(self):
        """
        Check if all asteroids have been mined, and regenerate if necessary.
        """
        if all(next(iter(asteroid.materials.values())) <= 0 for asteroid in self.asteroids):
            print("\nAll asteroids have been mined. Regenerating asteroid belt...")
            self.asteroids = self._generate_asteroids()

    def _display_asteroids(self):
        """
        Print the materials and their amounts for each asteroid.
        """
        for i, asteroid in enumerate(self.asteroids, start=1):
            material, amount = next(iter(asteroid.materials.items()))
            print(f"Asteroid {i}: {amount} units of {material}")

    def _user_select_asteroid(self):
        """
        Prompt the user to select an asteroid.

        Returns:
            Asteroid: The selected Asteroid object.
        """
        while True:
            try:
                selected = int(input("Select an asteroid to mine: ")) - 1
                if 0 <= selected < len(self.asteroids):
                    return self.asteroids[selected]
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
