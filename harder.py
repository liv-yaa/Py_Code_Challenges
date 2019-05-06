""" Harder coding challenges 

"""


""" Object-Oriented Battleship
https://fellowship.hackbrightacademy.com/materials/challenges/battleship/index.html#battleship
"""

print('test')

import random
import sys

# For small screens
TIGHT = True

# Colors
NO_COLOR = False  # If the colors annoy you, set this to True

WATER = lambda msg: ('\033[34m%s\033[0m' % msg
                     if sys.stdout.isatty() and not NO_COLOR else msg)
SUNK = lambda msg: ('\033[91m%s\033[0m' % msg
                    if sys.stdout.isatty() and not NO_COLOR else msg)
HIT = lambda msg: ('\033[31m%s\033[0m' % msg
                   if sys.stdout.isatty() and not NO_COLOR else msg)


#####################################################################################

class Ship(object):
    ''' Type of ship.'''

    _length = 0 # length of ship
    name = ""   # Name of ship
    coords = [] # List of (col, row) coordinates where this ship is

    def __init__(self):
        assert self._length > 0 and self.name, "Must subclass with length and name!"

        self.hits = 0
        self.coords = []


    def is_sunk(self):
        ''' Is this ship sunk? '''        
        return self.hits == self._length

    def place(self, col, row, direction):
        ''' Place ship.
        Given a row & column direction, determine coordinates ship will occupy
        Update its coordinates property.
        Raises an exception for an illegal direction.

        This is meant to be an abstract class--you should subclass it
        for individual ship types.

            >>> class TestShip(Ship):
            ...     _length = 3
            ...     name = "Test Ship"

        Let's make a ship and place it:

            >>> ship = TestShip()

            >>> ship.place(1, 2, "H")
            >>> ship.coords
            [(1, 2), (2, 2), (3, 2)]

            >>> ship.place(1, 2, "V")
            >>> ship.coords
            [(1, 2), (1, 3), (1, 4)]

        Illegal directions raise an error:

            >>> ship.place(1, 2, "Z")
            Traceback (most recent call last):
            ...
            ValueError: Illegal direction

        '''













