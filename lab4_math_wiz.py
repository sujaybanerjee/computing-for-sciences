"""
CSCI150 Fall 2021 Lab 4

Name: Sujay Banerjee
Section: A

Creativity:

random_equation_flexible, random_equation_parens, query_equation_creativity, play_game2
"""

from random import randint
import random
import time

OPERATORS = ["+", "-", "*"]


def random_equation(num_operators):
    """
    Generates a random equation using all operators
    
    Args:
        num_operators: number of operators used in equation
    
    Returns:
        random equation as a string  
    """
#     equation = ''
#     for i in range(num_operators):
#         equation += "(" + str(randint(1,10)) + random.choice(OPERATORS)
#     equation += str(randint(1,10)) + ")"
#     return equation
    return random_equation_flexible(num_operators, OPERATORS)


def random_equation_flexible(num_operators, operators):
    """
    Generates a random equation using specified operator
    
    Args:
        num_operators: number of operators used in equation
        operators: specified operator to play game with
    
    Returns:
        random equation as a string  
    """
    equation = ''
    for i in range(num_operators):
        equation += str(randint(1,10)) + random.choice(operators)
    equation += str(randint(1,10))
    return equation

def random_equation_parens(num_operators, operators):
    """
    Generates a random equation using specified operator and parentheses that does not change end value
    
    Args:
        num_operators: number of operators used in equation
        operators: specified operator to play game with
    
    Returns:
        random equation with parentheses as a string
    """
    equation = '('
    for i in range(num_operators):
        op = random.choice(operators)
        if op == "*":
            equation += str(randint(1,10)) + op
        else:
            equation +=  str(randint(1,10)) + ")" + op + "("
    equation += str(randint(1,10)) +")"
    return equation





def query_equation(eq):
    """
    Determines if inputed answer to equation is correct, within 2 of being correct, or incorrect
    
    Args:
        eq: equation to evaluate
    
    Returns:
        none
    """
    correct_answer = eval(eq)
    correct = False
    while not correct:
        answer = int(input(eq + " = "))
        if answer == correct_answer:
            print("Correct!")
            correct = True
        elif answer-2 <= correct_answer <= answer+2:
            print("Close. Try again")
            #return query_equation(eq)

        else:
            print("Keep trying.")
            #return query_equation(eq)
      
      
def query_equation_creativity(eq):
    """
    Determines if inputed answer to equation is correct, higher or lower
    
    Args:
        eq: equation to evaluate
    
    Returns:
        none
    """
    correct = False
    while not correct:
        answer = int(input(eq + " = ")) 
        if answer == eval(eq):
            print("Correct!")
            correct = True
        elif answer > eval(eq):
            print("Lower. Keep trying")
            #return query_equation(eq)
        else:
            print("Higher. Keep trying")
            #return query_equation(eq)

                
            
def play_game(duration, num_operators):
    """
    Presents user with new equations to answer and increases count when correct
    
    Args:
        duration: length of game in seconds
        num_operators: number of operators used in equation
    
    Returns:
        none
    """
    initial = time.time()
    count = 0
    while time.time() - initial <= duration:
        query_equation_creativity(random_equation(num_operators))
        count += 1
    print("You got", count, "correct in", time.time() - initial, "seconds.")
    
    
def play_game2(duration, num_operators, operators):
    """
    Presents user with new equations with specified operators to answer and increases count when correct
    
    Args:
        duration: length of game in seconds
        num_operators: number of operators used in equation
        operators: specified operator to play game with
        
    
    Returns:
        none
    """
    initial = time.time()
    count = 0
    while time.time() - initial <= duration:
        query_equation_creativity(random_equation_flexible(num_operators, operators))
        count += 1
    print("You got", count, "correct in", time.time() - initial, "seconds.")
    
    
    
def main():
    """Launch the math wiz game, including asking user if they want to play"""
    play = input("Do you want to play a game [yes/no]? ")
    if play.lower() == "no":
        print("Goodbye, have a nice day.")
    else:
        duration = int(input("How long do you want to play the game for [seconds]? "))
        num_operators = int(input("Select the difficulty level from 1-10: "))
        operator = input("Which operator to you want to play with [all, +, -, *]? ")
        if operator == "all":
            play_game(duration, num_operators)
        elif operator == "+":
            play_game2(duration, num_operators, ["+"])
        elif operator == "-":
            play_game2(duration, num_operators, ["-"])
        else:
            play_game2(duration, num_operators, ["*"])
   

if __name__ == '__main__':
    main()
    
    
    

        
    
    
    
    
    
    
    