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
    ships = []

    # Methods
    def __init__(self):
        """ Constructor for Battleship class 
        Populates shipes list with random coordinates
        """
        # self.ships = [
        #     (1, 1),
        #     (1, 2), 
        #     (3, 4),
        #     (4, 5),

        # ]
        


    def play(self):
        """ Method for playing game """
        print('Playing game...')



# To get warmed up just copying

# Greate list of ship positions as data structure
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


def build_board(board):
    # Build a 5 x 5 board
    board = ['0'] * 5


def show_board(board):
    print('Find and sink the ship!')
    for row in board:
        print(" ".join(row))


def play_game(board):
    print('Welcome to Battleship')
    
    # Clear board
    del board[:]

    # 
    build_board(board)

    # Show board
    show_board(board)

    # Assign random numbers to 'guess':
    ship_col = randint(1, len(board))
    ship_row = randint(1, len(board[0]))

    return {
        'ship_col': ship_col,
        'ship_row': ship_row,
    }

ship_points = play_game(game_board)


def take_turns(total_turns):
    """ Alternate taking """

    if total_turns % 2 == 0:
        total_turns += 1
        return player_1

    else:
        return player_2



def play_again():
    """ Allow a new game to start """

    global ship_points

    answer = input('Play again? ')

    if answer == 'yes' or answer == 'y':
        ship_points = load_game(game_board)

    else:
        print('Bye')
        exit()


def input_check(ship_row, ship_col, player, board):

    guess_col = 0
    guess_row = 0


    while True:
        try:
            guess_row = int(input('Guess Row: ')) - 1
            guess_col = int(input('Guess Col: ')) - 1

        except ValueError:
            print('Enter a number only')
            continue

        else:
            break

    # Assign some boolean values based on the result
    match = guess_row == ship_row - 1 and guess_row == ship_col - 1\
    not_on_board = (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)

    # Results
    if match:
        # Increment wins!
        player['wins'] += 1 

        print("Congratulations! You sunk my battleship!")
        print('The current match score is %d : %d (Player1 : Player2)' % (player_one["wins"], player_two["wins"]))
        print("Thanks for playing!")

        # play again
        play_again()

    elif not match:
        if not_on_board:
            print("OOps, not in oacean")

        elif board[guess_row][guess_col] == 'X' or board[guess_row][guess_col] == 'Y':
            print('You already guessed that!')

        else:
            print('You missed the ship.')

            if player == player_1:
                board[guess_row][guess_col] == 'X'

            else:
                board[guess_row][guess_col] == 'Y'

        show_board(game_board)

    else:
        return 0


def main():
    begin = input('Type \'start\' to begin: ')


    while (begin != str('start')):
        begin = input('Type \'start\' to begin: ')


    for games in range(3):
        for turns in range(6):

            if player_turns(turns) == player_one:
                # print(ship_points)
                print("Player One")
                input_check(
                    ship_points['ship_row'],
                    ship_points['ship_col'],
                    player_one, game_board
                )

            elif player_turns(turns) == player_two:
                print("Player Two")
                input_check(
                    ship_points['ship_row'],
                    ship_points['ship_col'],
                    player_two, game_board
                )

            if turns == 5:
                print("The number of turns has ended.")
                print('The current match score is %d : %d (Player1 : Player2)' % (player_one["wins"], player_two["wins"]))
                play_again()






if __name__ == '__main__':

    # Create instance of game 
    game1 = Battleship()

    # Call class method to play game?
    game1.play()

    # Call method to 