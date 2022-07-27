#! /usr/bin/env python3

"""
Auther: Micah McConnaughey
PyEve Version 1
Date: 07/27/2022
Python 3.7
"""

import random


class Player:
    def __init__(self, name):
        self.name = input("Name: ") 


class Station:
    def __init__(self, name, cargo_bay):
        self.name = name
        self.cargo_bay = cargo_bay
        
    def dock(self):
        dock = input('Dock the ship? ')
        if dock == 'y':
            return True
        return False


class Ship:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def enter(self):
        enter_ship = input('Enter the ship? ')
        if enter_ship == 'y':
            return True
    
    def exit(self):
        exit = input('Exit the ship? ')
        if exit == 'y':
            return True
        return False
    
    def fly(self):
        pass
        

class Tool:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Astroid:
    def __init__(self, name, type, mass=10):
        self.name = name
        self.type = type
        self.mass = mass


class Ore:
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity
