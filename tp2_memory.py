"""
CSCI150 Test Project 2

Name: Sujay Banerjee
Section: A
"""

import random
import time
import sys


ALPHABET = "AABBCCDDEEFFGGHHIIJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
NUM_ROWS = 4
NUM_COLS = 4
COL_WIDTH = 2




def num_to_letter(NUM_ROWS, NUM_COLS):
    """
    Creates a tuple of a list of numbers and a list of letters from a dictionary to be the base for the board

    Args:
        NUM_ROWS: constant of number of rows on board
        NUM_ROWS: constant of number of columns on board
    
    Returns:
        tuple of a list of numbers and a list of letters
    """
    numbers = []
    letters = []
    maps = {}
    for i in range(NUM_ROWS*NUM_COLS):
        numbers.append(i+1)
    for i in range(len(numbers)):
        letters.append(ALPHABET[i])
        maps[numbers[i]] = letters[i]
    answer_board = list(maps.values())
    working_board = list(maps.keys())
    random.shuffle(answer_board)
    return (working_board, answer_board)




def print_board(working_board):
    """
    Prints the board from the working_board list

    Args:
        working_board: list of board numbers or letters

    
    Returns:
        none
    """
    count = 0
    for spot in working_board:
        print(str(spot).ljust(COL_WIDTH), end = " ")
        count += 1
        if count % NUM_COLS == 0:
            print(end = "\n")

        
            

def replace_board(board, guess1, guess2):
    """
    Replaces the values in the working board based on the guesses

    Args:
        board: tuple of board numbers and letters
        guess1: first number guess
        guess2: second number guess

    
    Returns:
        updated working_board list
    """
    working_board = board[0]
    answer_board = board[1]
    if guess1 and guess2 in working_board:  
        working_board[guess1-1] = answer_board[guess1-1]
        working_board[guess2-1] = answer_board[guess2-1]
    return working_board
    
      
            
    
def play_game():
    """
    Calls previous functions and creates game loop to be able to play

    Args:
        none
        
    Returns:
        none
    """
    board = num_to_letter(NUM_ROWS, NUM_COLS)
    working_board = board[0]
    answer_board = board[1]
    turns = 0
    start = time.time()
    while working_board != answer_board:
        print_board(working_board)
        guess1, guess2 = input("Guess two squares:").split()
        guess1 = int(guess1)
        guess2 = int(guess2)
        if guess1 in working_board and guess2 in working_board and guess1 != guess2:
            if answer_board[guess1-1] == answer_board[guess2-1]:
                working_board = replace_board(board, guess1, guess2)
                print_board(working_board)
                for i in range(100):
                    print("\n")
            else:
                working_board = replace_board(board, guess1, guess2)
                print_board(working_board)
                time.sleep(2) 
                working_board[guess1-1] = guess1
                working_board[guess2-1] = guess2
                for i in range(100):
                    print("\n")
            turns += 1
        else:
            print("Invalid number(s).")
    finish = time.time()
    print("You win!")
    print_board(working_board)
    print("It took you ", str(turns), " guesses and ", str(int(finish - start)), "seconds.")
        
        
            
                
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        play_game()


        

            
        



