class Person:

    skill = 0
    hit_points = 10
    armor = 1

    def __init__(self, name) -> None:
        self.name = name


class Ship:

    in_ship = False
    armor = 10

    def __init__(self, model) -> None:
        self.model = model

    def enter_car(self) -> None:
        Ship.in_ship = True

    def exit_car(self) -> None:
        Ship.in_ship = False


def ask() :
    enter = input('Enter car? ')
    if enter == 'y':
        ship.enter_car()
        print(f'{person.name} is in the {ship.model}!')


person = Person('Attwood')
ship = Ship('Ship')
ask()
