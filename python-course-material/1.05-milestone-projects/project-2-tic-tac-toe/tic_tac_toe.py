board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"] # Normal list, written as grid for better understanding

player = "X" # We use one variable and change the player between "X" and "O"

# A function that returns if the whole grid is full or not (bool)
def game_over():

    game_over = ""

    for cell in board:
        if cell not in ["X", "O"]: # Checks if there are other things in the list other than "X" and "O"
            game_over = False
            break # Since there are still cell numbers in the list, we know its not game over so we return false and break
        else: 
            game_over = True # If it is an "X" or "O" we return true
            continue # We continue to the next loop

# The logic here is that if there is on cell that is a number we know that the game is still going...
# When the cell is an "X" or "O" is returns true and continues, if the there is a number we make it false and break the loop..
# if not we continue to reassign it as true and if no number are present we return true
    return game_over

while True:

    if game_over():
        print("Game Over!") # If game_over() returns True we end the game and break the loop
        
        # Print final table!
        print("")
        print(board[0], "|", board[1], "|", board[2]) 
        print("----------")
        print(board[3], "|", board[4], "|", board[5])
        print("----------")
        print(board[6], "|", board[7], "|", board[8]) 

        break
    else:
        print("")
        print(board[0], "|", board[1], "|", board[2]) # You can user either + or , to join together the list cells and the union character
        print("----------")
        print(board[3], "|", board[4], "|", board[5])
        print("----------")
        print(board[6], "|", board[7], "|", board[8]) # keep in mind that even thought the last cell is 9, its index is 8 as index always starts with 0


        move = input(f"Player {player}, choose a valid spot from 1-9: ")

        # Check if the user entered a valid input, if not continue to the next loop
        if not move.isdigit(): 
            print("Enter a valid number!")
            continue

        move = int(move) # Reassign the move from str to int

        # Check if the user entered a valid number that is higher than 9 (outside grid range)
        if move > 9:
            print("Enter a valid number!")

        if board[move - 1] not in ["X", "O"]: # Checks if the cell is not taken by an "X" or an "O"
            board[move - 1] = player

        if player == "X": # Checks if the current player is "X"
            player = "O" # Then reassigns it as "O"
        else:
            player = "X" # If player is "O" then we reassign the player as "X"

