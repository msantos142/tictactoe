import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# draw the board
def display_board(board):
    # draw the board
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |     ')

# get player input 
def player_input():

    # will return tuple (player 1 marker, player 2 marker)
    marker = ''

    # make sure it is either a 'X' or an 'O
    while marker !='X' and marker !='O':
        marker = input('Player 1, enter the mark you want to use (X or O): ').upper()   

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

# put new mark on board
def place_marker(board, marker, position):
    cls()
    board[position] = marker
    display_board(board)

# check if player wins
def win_check(board, mark):
	# list to store index of found marks
    combinations = [[7,8,9],[4,5,6],[1,2,3],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for a,b,c in combinations:
        if board[a] == board[b] == board[c] == mark:
            return True 
    return False
    
# choose player who goes first
def choose_first():
    play_first = random.randint(1,2)
    print('Player {0} goes first!'.format(play_first))
    return play_first

# check if space is occupied
def space_check(board, position):
    # returns True if space is free
    # meaning, the space isn't occupied by an 'X' or 'O'
    return board[position] == ' '

# check if board is full
def full_board_check(board):
    # if board has less then 1 spaces to occupy
    return board.count(' ') < 1

# ask for player position and check if it's free
def player_choice(board):
    choice = ''
    acceptable_range = range (1,10)
    within_range = False

		# keep asking for input until it is a digit and within the range
    while choice.isdigit() == False or within_range == False:
        choice = input('Please, select a position (1-9): ')
        # if it's not a number inform the user
        if choice.isdigit() == False:
            print('Sorry, that is not a valid position!')

        if choice.isdigit() == True:
        		# if it's a digit check if it's in acceptable range
            if int(choice) in acceptable_range:
            		# check if spot is available to claim
                if space_check(board, int(choice)):
                    within_range = True
                else:
                    within_range = False
                    print('Sorry, that position has been taken!')
            else:
            		# not necessary but included for legibility
                within_range = False    

    return int(choice)

# asks the player if they want to play again and returns a boolean True if they do want to play again
def replay():
    
    play_again = ''

    while play_again !='Y' and play_again !='N':
        play_again = input('Would you like to play again? (Y/N): ').upper()

    return play_again == 'Y'

############
##  Game  ##
############

print('Welcome to Tic Tac Toe! \n')

while True:
    # Set the game up here
    game_on = True       
    # populate board with spaces and display it
    game_board = [' '] * 10
    cls()
    display_board(game_board)
    # have players decide their marker
    player1, player2 = player_input()
    first_to_play = choose_first()
    # store marks ordered
    marks = ()
    if first_to_play == 1:
        marks = (player1, player2)
    else: 
        marks = (player2, player1)

    while game_on: 
        # alternate between players 
        for m in marks:
            # get player chosen position (pos) and place marker
            pos = player_choice(game_board)
            place_marker(game_board, m, pos)
            # check if game is over
            if win_check(game_board, m) or full_board_check(game_board):
                if win_check(game_board, m):
                    if player1 == m:
                        print('The winner is Player 1!')
                    else:
                        print('The winner is Player 2!')
                    
                else:
                    print("It's a tie!")
                game_on = False
                break

    if not replay():
        break
