#Sujay Banerjee
#Space Scene


from turtle import *
from random import randint

# Creativity section: def stars, def isosceles_triangle, def comet, def satellite


def generate_picture():
    """ Function that draws the complete picture
        
        Args:
            None
      
      Returns:
            None
    """
    bgcolor("black")
    pencolor("black")
    stars(30, 10, "yellow")
    stars(30, 10, "white")
    add_circles(20)
    comet("gray", 10, 200,-100)
    satellite(0,-100,"gray")
    triangle(30, "red", 100,100)
    triangle(40, "blue", 250,250)
    triangle(25, "green", 280,-200)
    isosceles_triangle(30, "white", -70,-20)
    isosceles_triangle(50, "pink", 0,200)
    isosceles_triangle(35, "lightblue", 0,-250)
    polygon(40, "purple", -150, 50)
    polygon(20, "blue", 20, 30)
    polygon(30, "red", -250, -230)
    circle_planet(15, "brown", 65, -270)
    circle_planet(30, "orange", 150, 200)
    circle_planet(35, "darkgreen", -200, 270)
    
    
    

def circle_planet(radius, color, x, y):
    """ Function that draws circular planets
        
        Args:
            radius as an int
            color as a string
            x, y as ints for position
      
      Returns:
            None
    """
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def polygon(size, color, x, y):
    """ Function that draws polygon planets
        
        Args:
            size as an int
            color as a string
            x, y as ints for position
      
      Returns:
            None
    """
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    for i in range(10): 
        forward(size)
        right(36)
    end_fill()

def add_circles(num_stars):
    """ Function that draws randomized positions and sizes of circles 
        
        Args:
            num_stars is the number of stars drawn
      
      Returns:
            None
    """
    for i in range(num_stars):
        c = randint(3, 6)
        penup()
        goto(randint(-340, 340), randint(-340, 340))
        pendown()
        circle_planet(c, "yellow", randint(-340, 340), randint(-340, 340))
        circle_planet(c, "white", randint(-340, 340), randint(-340, 340))
    
def stars(stars_num, size, color):
    """ Function that draws randomized positions and size of stars using 2 triangles
        
        Args:
            stars_num is the number of stars
            color as a string
      
      Returns:
            None
    """
    for i in range(stars_num):
        pencolor("white")
        penup()
        x = randint(-340, 340)
        y = randint(-340, 340)
        size = randint(8,13)
        goto(x, y)
        pendown()
        fillcolor(color)
        begin_fill()
        for j in range(3):
            forward(size)
            right(120)
        end_fill()
        penup()
        goto(x, y-6)
        pendown()
        fillcolor(color)
        begin_fill()
        for k in range(3):
            forward(size)
            left(120)
        end_fill()
        
            
        

def triangle(size, color, x, y):
    """ Function that draws equilateral triangles as spaceships
        
        Args:
            size as an int
            color as a string
            x, y as ints for position
      
      Returns:
            None
    """
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    left(90)
    for i in range(3): 
        forward(size)
        right(120)
    end_fill()
    
def isosceles_triangle(size, color, x, y):
    """ Function that draws isosceles triangles as spaceships
        
        Args:
            size as an int
            color as a string
            x, y as ints for position
      
      Returns:
            None
    """
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    right(20)
    forward(size)
    right(140)
    forward(size)
    right(110)
    forward(size-20)
    end_fill()

   
def comet(color, length, x, y):
    """ Function that draws an irregular polygon as a comet
        
        Args:
            length as an int
            color as a string
            x, y as ints for position
      
      Returns:
            None
    """
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    for i in range(12):
        forward(length+10)
        right(40)
        forward(length)
        left(70)
    end_fill()
    penup()
    goto(x+10, y+15)
    circle_planet(6, "black", x+10, y+15)
    penup()
    goto(x+40, y+60)
    circle_planet(8, "black", x+40, y+60)
    penup()
    goto(x+50, y+15)
    circle_planet(8, "black", x+55, y+15)
    
    
def satellite(x, y, color):
    """ Function that draws a satellite
        
        Args:
            color as a string
            x, y as ints for position
      
      Returns:
            None
    """
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    left(180)
    for i in range(3):
        left(60)
        forward(30)
    end_fill()
    penup()
    goto(x+35, y+15)
    pendown()
    fillcolor(color)
    begin_fill()
    left(60)
    for i in range(3):
        right(60)
        forward(30)
    end_fill()
    penup()
    goto(x+11, y-19)
    pendown()
    fillcolor(color)
    begin_fill()
    left(148)
    forward(39)
    right(90)
    forward(15)
    right(90)
    forward(39)
    right(90)
    forward(15)
    end_fill()
        
    
        

    
        
        