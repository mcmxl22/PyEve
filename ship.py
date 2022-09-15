class Ship:

    in_ship = False
    armor = 10

    def __init__(self, type, name) -> None:
        self.type = type
        self.name = name

    def enter_ship(self) -> bool:
        Ship.in_ship = True
        return Ship.in_ship

    def exit_ship(self) -> bool:
        Ship.in_ship = False
        return Ship.in_ship
