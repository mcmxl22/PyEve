from dataclasses import dataclass


@dataclass
class Config:
    """Configure ship information."""
    ship_type = str
    ship_name = str


class Ship(Config):
    """Define a ship"""
    in_ship = False
    armor = 10

    def enter_ship(self) -> bool:
        Ship.in_ship = True
        return Ship.in_ship

    def exit_ship(self) -> bool:
        Ship.in_ship = False
        return Ship.in_ship
