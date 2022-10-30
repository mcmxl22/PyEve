from character import Person
from Menu import Menu
from ship import Ship, Config


def main():
    """Main function."""

    player = Person("John Doe")
    Config.ship_name = "Venture"
    Config.ship_type = "miner"
    ship = Ship()
    menu = Menu.list_choices(
        [
            "Exit",
            "Enter",
            "Quit"
        ]
    )

    print(f"Welcome to PyEve {player.name}!")
    print(f"Here is your first ship, a {ship.ship_type}.")

    enter_ship = ship.enter_ship()

    if enter_ship == True:
        print(f"You are now in the {ship.ship_name}.")


if __name__ == "__main__":
    main()
