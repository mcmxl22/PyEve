import time
from mining_laser import MiningLaser


class Spaceship:
    """Represent a spaceship with cargo capacity and a mining laser."""

    def __init__(self, cargo_capacity, laser):
        """
        Initialize a Spaceship instance.

        Args:
            cargo_capacity (int): Maximum cargo capacity of the spaceship.
            laser (MiningLaser): Mining laser equipped on the spaceship.
        """
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0
        self.docked = True
        self.laser = laser

    def load_cargo(self, amount):
        """
        Load cargo into the spaceship's cargo hold.

        Args:
            amount (int): Amount of cargo to be loaded.

        Returns:
            bool: True if the cargo is successfully loaded, False otherwise.
        """
        if self.current_cargo + amount <= self.cargo_capacity:
            self.current_cargo += amount
            return True
        else:
            return False

    def unload_cargo(self):
        """
        Unload the spaceship's cargo.

        Returns:
            int: Amount of cargo that was unloaded.
        """
        unloaded_material = self.current_cargo
        self.current_cargo = 0
        return unloaded_material

    def dock(self):
        """
        Dock the spaceship at the space station.

        Power off the mining laser if it is powered on.
        """
        self.docked = True
        print("Spaceship docked at the space station.")
        if self.laser.is_powered:
            self.laser.power_off()
            print("Mining laser powered off.")

    def mine(self, asteroid):
        """
        Mine an asteroid using the spaceship's mining laser.

        Args:
            asteroid (Asteroid): Asteroid to be mined.
        """
        if self.docked:
            print("Cannot mine while docked. Please undock first.")
            return

        self.laser.power_on()

        while self.laser.is_powered:
            if self.current_cargo >= self.cargo_capacity:
                self.laser.power_off()
                print(self.current_cargo)
                print("\nCargo is full.")
                return

            material, amount = next(iter(asteroid.materials.items()))
            if amount <= 0:
                self.laser.power_off()
                print(f"\nAsteroid's {material} has been depleted.")
                return

            time.sleep(self.laser.cycle_time)
            available_space = self.cargo_capacity - self.current_cargo
            mined_material = min(self.laser.power, amount, available_space)
            mined_material = max(mined_material, 0)

            if mined_material > amount:
                mined_material = amount

            if mined_material > available_space:
                mined_material = available_space
                self.current_cargo = self.cargo_capacity

            asteroid.materials[material] -= mined_material
            self.current_cargo += mined_material

            print(f"\rMined: {mined_material} units of {material}, Remaining in Asteroid: {asteroid.materials[material]}, "
                  f"Space Remaining in Cargo: {self.cargo_capacity - self.current_cargo}\n", end='', flush=True)
