"""
CSCI150 Lab 6

Name: Sujay Banerjee, Tucker Lamb
Section: A

Creativity:
Checks for errors and makes sure user uses valid input when playing the game.
Created hangman drawing to represent how many guesses the user has gotten incorrect. Game ends when hangman drawing is completed.
"""

from random import randint
import random
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
default = 7


def play_wordgame(filename, num_incorrect_allowed):
    """
    Play wordgame

    Args:
        filename: File of words to use in game
        num_incorrect_allowed: Number of incorrect guesses permitted
    """
    words = read_words(filename)
    answer = words[randint(0, len(words)-1)]
    current = "_" * len(answer)
    word = set()
    while num_incorrect_allowed != 0:
        check = True
        print("-----------------")
        print("Guessed letters:", set_to_string(word).upper())
        print("Incorrect guesses left:", "*" * num_incorrect_allowed)
        print("Word:", current, "\n")
        draw_hangman(default-num_incorrect_allowed)
        while check:
            letter = input("Guess a letter:").lower()
            
            if letter not in ALPHABET:
                print("Please guess a letter")
            if letter not in word:
                check = False
            else:
                print("Letter already guessed!")
        word.add(letter)
        if letter in answer:
            current = insert_letter(letter, current , answer)
        else:
            if letter not in ALPHABET:
                num_incorrect_allowed = num_incorrect_allowed
            else:
                num_incorrect_allowed -= 1
        if answer == current:
            print("You win!")
            print("The word was:", answer)
            print("You guessed it with", default - num_incorrect_allowed, "incorrect guesses")
            exit()
        
    print("\nThe word was:", answer)
    print("Better luck next time!")
    
   
def draw_hangman(num_incorrect_allowed):
    """
    Draws pieces of hangman until the number of incorrect guesses reaches the max.

    Args:
        num_incorrect_allowed: Number of incorrect guesses permitted
        
    Returns: none
    """
    if num_incorrect_allowed == 1:
        print("  [ ]" + "\n")
    elif num_incorrect_allowed == 2:
        print("  [ ]" + "\n")
        print("   | "+ "\n")
    elif num_incorrect_allowed == 3:
        print("  [ ]" + "\n")
        print("\-----/ " + "\n")
        print("   | "+ "\n")
    elif num_incorrect_allowed == 4:
        print("  [ ]" + "\n")
        print("\-----/ " + "\n")
        print("   | "+ "\n")
        print("  /    ")
    elif num_incorrect_allowed == 5:
        print("  [ ]" + "\n")
        print("\-----/ " + "\n")
        print("   | "+ "\n")
        print("  / \  ")
    elif num_incorrect_allowed == 6:
        print("  [ ]" + "\n")
        print("\-----/ " + "\n")
        print("   | "+ "\n")
        print("  / \  ")
        print(" -  ")
    elif num_incorrect_allowed == 7:
        print("  [ ]" + "\n")
        print("\-----/ " + "\n")
        print("   | "+ "\n")
        print("  / \  ")
        print(" -   -")
        
   
def read_words(filename):
    """
    Opens file and creates random list of words.

    Args:
        filename
        
    Returns: list of words
    """
    word = []
    with open(filename, "r") as data_file:
        lines = data_file.read().split()
        return lines
        #word.append(random.choice(lines))
        #return word
       
                
def set_to_string(word):
    """
    Takes a set and converts it to a string.

    Args:
        set of words
        
    Returns: string of words
    """
    string = ''
    for letter in word:
        string += str(letter).upper() + " "
    return string


def list_to_string(word):
    """
    Takes a list and converts it to a string.

    Args:
        list of words
        
    Returns: string of words
    """
    string = ''
    for letter in word:
        string += str(letter)
    return string


def insert_letter(letter, current, answer):
    """
    Changes current to show correct letters guessed and their placement within the word..

    Args:
        letter guessed, updated progress, word answer
        
    Returns: updated progress
    """
    index = []
    current = list(current)
    for i in range(len(answer)):
        if answer[i] == letter.lower():
            current[i] = letter.lower()
    current = list_to_string(current)
    return current

     

if __name__ == '__main__':
    play_wordgame("cs_words.txt", default)