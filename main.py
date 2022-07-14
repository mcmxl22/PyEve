import PyEve as pe

def exit_game():
    """Exit game."""
    pass


def main():
    """Main function."""
    player = pe.Player('')
    ship = pe.Ship('AdVenture', 'Miner')
    print(f"Welcome to PyEve {player.name}!")
    print(f'Here is your first ship, a {ship.name}. It is a {ship.type}.')
    enter_ship = ship.enter()
    if enter_ship == True:
        print(f'You are in your {ship.name}.')
    else:
        print(f'You are not in your {ship.name}.')
        return enter_ship


if __name__ == '__main__':
    main()
