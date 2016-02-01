from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship! [Press Enter]"
raw_input("")
print "Hello comrade. I have a mission for you."
raw_input("")
print "Here is the ocean (Looking rather rectangular)"
print_board(board)
raw_input()
print "Your task is to find the enemy's battleship and attack it with a bomb. You will win once their battleship is sunken. You have 11 bombs."
raw_input()
print "Commencing mission..."
print "Your country depends on you, comrade."

def random_row(board):
    return randint(0, len(board) - 1)
    

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
col_or_row = randint(0,1)



if col_or_row == 0 :
    if ship_row < 3 :
        Ship_Row = [ship_row, ship_row + 1, ship_row +2]
    else :
        Ship_Row = [ship_row, ship_row - 1, ship_row -2]
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    for turn in range(11):
        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        
        if (guess_row - 1 == Ship_Row[0] and guess_col -1== ship_col) or (guess_row-1 == Ship_Row[1] and guess_col-1 == ship_col) or (guess_row-1 == Ship_Row[2] and guess_col-1== ship_col) :
            print "Yes! You've hit the enemy's battleship!"
            board[guess_row-1][guess_col-1] = "H"
            print_board(board)
            if board[Ship_Row[0]][ship_col] == "H" and board[Ship_Row[1]][ship_col] == "H" and board[Ship_Row[2]][ship_col] =="H" :
                print
                print print_board(board)
                print "Congratulations, Soldier, you've sunk the enemy's battleship!"
                break
        else:
            if (guess_row-1 < 0 or guess_row-1 > 4) or (guess_col-1 < 0  or guess_col-1 > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row-1][guess_col-1] == "X"):
                print "You guessed that one already."
            else:
                print "You missed the enemy's battleship!"
                board[guess_row-1][guess_col-1] = "X"
                if turn == 11 : 
                    print "Game Over"
            # Print (turn + 1) here!
            print_board(board)
            
            
if col_or_row == 1 :
    if ship_col < 3 :
        Ship_Col = [ship_col, ship_col + 1, ship_col +2]
    else :
        Ship_Col = [ship_col, ship_col - 1, ship_col -2]
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    for turn in range(11):
        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        
        if (guess_col - 1 == Ship_Col[0] and guess_row -1== ship_row) or (guess_col-1 == Ship_Col[1] and guess_row-1 == ship_row) or (guess_col-1 == Ship_Col[2] and guess_row-1== ship_row) :
            print "Yes! You've hit the enemy's battleship!"
            board[guess_row-1][guess_col-1] = "H"
            print_board(board)
            if board[ship_row][Ship_Col[0]] == "H" and board[ship_row][Ship_Col[1]] == "H" and board[ship_row][Ship_Col[2]] =="H" :
                print
                print print_board(board)
                print "Congratulations, soldier, you've sunk the enemy's battleship!"
                break
        else:
            if (guess_row-1 < 0 or guess_row-1 > 4) or (guess_col-1 < 0  or guess_col-1 > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row-1][guess_col-1] == "X"):
                print "You guessed that one already."
            else:
                print "You missed the enemy's battleship!"
                board[guess_row-1][guess_col-1] = "X"
                if turn == 11 : 
                    print "Game Over"
            # Print (turn + 1) here!
            print_board(board)
