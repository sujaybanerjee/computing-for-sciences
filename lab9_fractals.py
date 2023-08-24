"""
CSCI 150 Lab 9 Fractals

Name: Sujay Banerjee
Section: A

Creativity:
added variable color based on levels to recursive_h
created sum_helper and sum_nested to take a nested list of integers and returns the sum of all the lists.


"""

from turtle import *

def gcd(a, b):
    """
    Uses Euclid’s algorithm to return the GCD of any two positive integer parameters
    
    Args:
        a, b: two positive integers
        
    Returns:
        greatest common divisor
    """
    rem = a % b
    if rem == 0:
        return b
    else:
        return(gcd(b, rem))
    
        
        
def stairs(length, levels):
    """
    Uses recursion to draw decreasing sized squares
    
    Args:
        length: length of each side
        levels: number of squares
        
    Returns:
        none
    """
    if levels > 0:
        forward(length)
        right(90)
        forward(length)
        left(90)
        stairs(length/2, levels-1)
        right(180)
        forward(length)
        right(90)
        forward(length)
        right(90)




def sierpinski(length, iterations):
    """
    Uses recursion to draw the Sierpinski Triangle
    
    Args:
        length: length of each side triangle
        iterations: number of generations drawn
        
    Returns:
        none
    """
    if iterations == 1:
        for i in range(3):
            forward(length)
            left(120)
    else:
        sierpinski(length/2, iterations-1)
        forward(length/2)
        sierpinski(length/2, iterations-1)
        left(120)
        forward(length/2)
        right(120)
        sierpinski(length/2, iterations-1)
        right(120)
        forward(length/2)
        left(120)
        


def recursive_h(length, level):
    """
    Uses recursion to draw recursive H
    
    Args:
        length: length of vertical bars
        levels: number of generations drawn
        
    Returns:
        none
    """
    previous_color = pencolor()
    if level == 0:
        dot("purple")
        return 0
    if level % 3 == 0:
        pencolor("blue")
    if level % 3 == 1:
        pencolor("red")
    if level % 3 == 2:
        pencolor("green")
    if level !=0: 
        forward(length*2)
        right(90)
        forward(length)
        left(90)
        recursive_h(length/2, level-1)
        left(90)
        forward(length*2)
        right(90)
        recursive_h(length/2, level-1)
        right(90)
        forward(length)
        right(90)
        forward(length*4)
        left(90)
        forward(length)
        right(90)
        recursive_h(length/2, level-1)
        right(90)
        forward(length*2)
        right(90)
        recursive_h(length/2, level-1)
        right(90)
        forward(length)
        left(90)
        forward(length*2)
    pencolor(previous_color)  
 

def sum_helper(a_list, sums):
    """
    Uses recursion to create list of extracted numbers from list
    
    Args:
        a_list: original list
        sums: extracted numbers list
        
    Returns:
        none
    """
    if type(a_list) != list:
        sums.append(a_list)
    else:
        for i in a_list:
            sum_helper(i,sums)
 
def sum_nested(a_list):
    """
    Computes the sum of list from sum_helper
    
    Args:
        a_list: original list
        
    Returns:
        sum of numbers
    """
    s = []
    sum_helper(a_list,s)
    return sum(s)


# When all is complete, create screenshot using
# drawing_demo()


# Testing code is provided below that calls the recursive functions above
        
def stairs_demo(length=256, levels=5):
    """
    Set up for stairs drawing and call stairs().

    First moves the turtle to the top left of the screen, then calls stairs()  
    to draw a staircase of squares. Calls turtle.done() at the end of drawing.
    
    Args:
        length: side length of top square in pixels 
        levels: number of boxes to draw 
    """
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    penup()
    goto(-window_width()/2 + 20, window_height()/2 - 20)
    pendown()    

    # draw the stairs by calling recursive function
    stairs(length, levels)

    # finished
    done()


def sierpinski_demo(length=300, iterations=5):
    """
    Set up for sierpinski drawing and call sierpinski().
    
    First moves the turtle to the left edge of the drawing window, turns off
    tracer, and then calls sierpinski(). Calls turtle.done() at end of drawing.
    
    Args:
        length: base length of Sierpinski triangle in pixels 
        iterations: complexity level of Sierpinski triangle 
    """
    if iterations > 3:
        # Turn off animation (too slow for many iterations)
        tracer(False)
    
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    penup()
    goto(-window_width()/3 + 20, 0)
    pendown()
    
    sierpinski(length, iterations)
    
    # finish
    update() # need update() if using tracer(False)
    done()     
    

def recursive_h_demo(length=150, level=3):
    """
    Set up for recursive_h drawing and call recursive_h().
    
    Turns tracer off, calls recursive_h(), and ends with turtle.done().
    
    Args:
        length: height of innermost H in pixels
        level: complexity level of recursive H
    """
    if level > 2:
        # Turn off animation (too slow for many iterations)
        tracer(False)
    
    recursive_h(length, level)
    
    update() # need update() if using tracer(False)
    done()
    

def drawing_demo():
    """
    Create drawings of `stairs`, `sierpinski`, and `recursive_h`.
    
    Args:
        None
    """
    tracer(False)
    
    # draw stairs in upper left of drawing window
    penup()
    goto(-window_width()/2 + 20, window_height()/2 - 20)
    pendown()    
    stairs(150, 6)
       
    # draw sierpinski in upper right of drawing window
    penup()
    goto(0, window_height()/2 - 300)
    pendown()    
    sierpinski(300, 5)
    
    # draw recursive H in lower half of drawing window
    penup()
    goto(0, -window_height()/4)
    pendown()    
    recursive_h(150, 4)
    
    # finish
    update() 
    done()     