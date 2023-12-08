from mining_laser import MiningLaser
from asteroid import Asteroid, AsteroidBelt
from spaceship import Spaceship
from space_station import SpaceStation
from user_account import UserAccount
import os

def main():
    user_account = UserAccount()
    
    while True:
        print("\nWelcome to Asteroid Miner!")
        print("Create a new account or log in.\n")
        
        while True:
            options = ("1. Register", "2. Login", "3. Exit")
            for i in options:
                print(i)

            account_action = input("\nChoose an option: ")

            if account_action == '1':
                user_account.register_account()

            elif account_action == '2':
                if user_account.login():
                    break
                else:
                    print("Invalid login. Try again.")

            elif account_action == '3':
                print("o7")
                return

            else:
                print("Invalid command. Enter a number between 1 and 3.")

        # Initialize game objects
        laser = MiningLaser(100, 5)
        spaceship = Spaceship(500, laser)
        station = SpaceStation(spaceship)
        asteroid_belt = AsteroidBelt()

        print("\nYou command a spaceship equipped with a mining laser.")
        print("Your goal is to mine as much material as possible.\n")
        print("Here are the basic commands:")
        print("  '1' - Mine: Undock from the space station and start mining")
        print("  '2' - Dock: Dock at the space station and unload your cargo.")
        print("  '3' - Upgrade: Use carbon in a space station to increase your cargo capacity.")
        print("  '4' - Exit: Quit game.\n")

        while True:
            options = ("1. Mine", "2. Dock", "3. Upgrade", "4. Exit")
            for i in options:
                print(i)
            command = input("\nChoose an option: ")

            if command == '1':
                station.undock_ship()
                if not spaceship.docked:
                    asteroid = asteroid_belt.select_asteroid()
                    spaceship.mine(asteroid)

            elif command == '2':
                station.dock_ship()
                print("Cargo unloaded: ", station.cargo_dock)
            
            elif command == '3':
                station.upgrade_spaceship()

            elif command == '4':
                os.system('cls')
                print("o7")
                raise SystemExit

            else:
                print("Invalid command. Enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
