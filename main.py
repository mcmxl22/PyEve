from character import Person
from Menu import Menu
from ship import Ship


def main():
    """Main function."""

    player = Person("Micah")
    ship = Ship("Miner", "Venture")
    menu = Menu.list_choices(
        [
            "Dock",
            "Enter",
            "Exit",
            "Fly",
            "Scan",
            "Refuel",
            "Repair",
            "Sell",
            "Buy",
            "Quit",
        ]
    )

    print(f"Welcome to PyEve {player.name}!")
    print(f"Here is your first ship, a {ship.name}.")

    enter_ship = ship.enter_ship()

    if enter_ship == True:
        print(f"You are now in the {ship.name}.")


if __name__ == "__main__":
    main()
