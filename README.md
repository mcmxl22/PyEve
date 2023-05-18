# PyEveAsteroid Miner Game
Description

Asteroid Miner is a simple text-based space mining simulation game. You command a spaceship equipped with a mining laser with the goal to mine as much material as possible from asteroids.
Gameplay

    Mine: Undock from the space station and start mining an asteroid.
    Return: Dock at the space station and unload your cargo.
    Exit: Quit the game.

Classes

    MiningLaser: Represents the mining laser equipped on the spaceship.
    Spaceship: Represents a spaceship with cargo capacity and a mining laser.
    SpaceStation: Handles the docking and undocking of a spaceship, and the transfer of cargo from the spaceship to the station.
    Asteroid: Represents an asteroid with a certain amount of material.
    AsteroidBelt: Represents a collection of asteroids.
    UserAccount: Represents a user account, which can be used to store player progress.

Files

    main.py: The main script to run the game.
    mining_laser.py: Contains the MiningLaser class.
    spaceship.py: Contains the Spaceship class.
    space_station.py: Contains the SpaceStation class.
    asteroid.py: Contains the Asteroid and AsteroidBelt classes.
    user_account.py: Contains the UserAccount class.
    cargo_data.json: Stores the current cargo data of the space station.

Running the Game

To play the game, run the main.py script.

css

python main.py

Future Work

    Add more types of spaceships and mining lasers.
    Add different kinds of asteroids with different materials.
