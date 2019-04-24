"""
'Battleship'

Practicing for a technical interview with Stride Health

by copying some demos 
- https://codereview.stackexchange.com/questions/164596/2-player-battleship-game-python
- https://codereview.stackexchange.com/questions/25541/designing-a-simple-battleship-game-in-python
but I am making a class+methods
"""

from random import randint

class Battleship:

    """ 
    Game of User vs Computer to try to sink ships.
    1. User types target coordinates 
    2. Computer answers if a ship has been hit or even if it has been sunk. 
    
    Ship positions are fixed (predefined in the program).

    """

    # Greate a board - list as data structure
    game_board = []

    # Initialize dicts to store info about players:
    player_1 = {
        'name': 'P1',
        'wins': 0,
        'lost': 0,
    }

    player_2 = {
        'name': 'P2',
        'wins': 0,
        'lost': 0,
    }


    # Methods
    def play(self):
        """ Method for playing game """
        print('Playing game...')




if __name__ == '__main__':

    # Create instance of game 
    game1 = Battleship()

    # Call class method to play game?
    game1.play()