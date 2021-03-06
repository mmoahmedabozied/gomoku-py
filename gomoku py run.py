N, M = 15, 15
a_row = 5
n_players = 2
marks = ['X', 'O']
grid = [[" " for i in range(N)] for j in range(N)]

#This function prints the grid of Gomoku as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if the game has a win state or not
def check_win():
    #check row
    for i in range(M-4):
        for j in range(N):
            if grid[j][i]=="X" and grid[j][i+1]=="X"  and grid[j][i+2]=="X"  and grid[j][i+3]=="X" and grid[j][i+4]=="X":
                return True
            if grid[j][i]=="O" and grid[j][i+1]=="O"  and grid[j][i+2]=="O"  and grid[j][i+3]=="O" and grid[j][i+4]=="O":
                return True
    #check colum
    for i in range(M):
        for j in range(N-4):
            if grid[j][i]=="X" and grid[j+1][i]=="X"  and grid[j+2][i]=="X"  and grid[j+3][i]=="X" and grid[j+4][i]=="X":
                return True
            if grid[j][i]=="O" and grid[j+1][i]== "O" and grid[j+2][i]== "O" and grid[j+3][i]== "O" and grid[j+4][i]=="O":
                return True
    #check diagonal
    for i in range(M-4):
        for j in range(N-4):
            if grid[j][i]=="X"  and grid[j+1][i+1]=="X"  and grid[j+2][i+2]=="X"  and grid[j+3][i+3]=="X" and grid[j+4][i+4]=="X" :
                return True
            if grid[j][i]== "O" and grid[j+1][i+1]== "O" and grid[j+2][i+2]== "O" and grid[j+3][i+3]== "O" and grid[j+4][i+4]=="O":
                return True
#This function checks if the game has a tie state or not for the given mark
def check_tie_player(mark):
    count=0
    for i in range(0,N):
       for j in range(0,M):
           if grid[i][j]!=" ":
               count+=1
    if count==225 and not check_win():
        return True

#This function checks if the game has a tie state or not
def check_tie():
    all_tie = True
    for mark in marks:
        if not check_tie_player(mark):
            all_tie = False
    return all_tie
	
#This function checks if given cell is empty or not 
def check_empty(i, j):
    if(grid[i][j]==" "):
     return True
    else:
      return False

#This function checks if given position is valid or not 
def check_valid_position(i, j):
   
        if(i in range(0,15) and j in range(0,15)):
          return True;
        else:
          return False;

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
    grid[i][j]=mark;

#This function clears the game structures
def grid_clear():
    for i in range (N):
     for j in range(M):
         grid[i][j]=" "

#This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i, j = read_input()
        #Set the player mark in the input position
        set_cell(i, j, marks[player])
        #Check if the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print('Congrats, Player %s is won!' % marks[player])
            break
        #Check if the grid has a tie state
        if check_tie():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = (player + 1) % n_players


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
