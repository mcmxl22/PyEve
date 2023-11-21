from mining_laser import MiningLaser
from asteroid import Asteroid, AsteroidBelt
from spaceship import Spaceship
from space_station import SpaceStation
from user_account import UserAccount

def main():
    # Initialize user account
    user_account = UserAccount()
    
    while True:
        print("\nWelcome to Asteroid Miner!")
        print("Please create a new account or log in.\n")
        
        while True:
            print("1. Register new account")
            print("2. Log in to existing account")
            print("3. Exit")

            account_action = input("\nChoose an option: ")

            if account_action == '1':
                user_account.register_account()

            elif account_action == '2':
                if user_account.login():
                    break
                else:
                    print("Invalid login credentials. Please try again.")

            elif account_action == '3':
                print("o7")
                return

            else:
                print("Invalid command. Please enter a number between 1 and 3.")

        # Initialize game objects
        laser = MiningLaser(100, 5)
        spaceship = Spaceship(500, laser)
        station = SpaceStation(spaceship)
        asteroid_belt = AsteroidBelt()

        print("\nYou command a spaceship equipped with a mining laser.")
        print("Your goal is to mine as much material as possible from asteroids.\n")
        print("Here are the basic commands:")
        print("  '1' - Mine: Undock from the space station and start mining an asteroid.")
        print("  '2' - Return: Dock at the space station and unload your cargo.")
        print("  '3' - Exit: Quit the game.\n")

        while True:
            print("\n1. Mine")
            print("2. Return to station")
            print("3. Exit")

            command = input("\nChoose an option: ")

            if command == '1':
                # Undock spaceship from station
                station.undock_ship()
                if not spaceship.docked:
                    # Select asteroid and start mining
                    asteroid = asteroid_belt.select_asteroid()
                    spaceship.mine(asteroid)

            elif command == '2':
                # Dock spaceship at station and unload cargo
                station.dock_ship()
                # Print the cargo unloaded to the station
                print("Cargo unloaded to the station: ", station.cargo_dock)

            elif command == '3':
                print("o7")
                raise SystemExit

            else:
                print("Invalid command. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
