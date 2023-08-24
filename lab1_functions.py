"""
CSCI150 Lab 1

Name: Sujay Banerjee
Section: A

Creativity:
<Provide a brief listing of your creativity additions so the graders know what to look for.>

function that converts eastern time to french time
used euros_to_dollars in dollars_to_euros
function that converts liters to gallons
used kilometers_to_miles and liters_to_gallons in mpg_from_metric

"""

# ---------------------- 
# Section 1: Functions that return a value
# ----------------------


def welcome():
    """Translates 'welcome' into french

     Args:
         parameters: none
         
    Returns:
         'welcome' in french
    """
    return "Bienvenue"



def euros_to_dollars(e):
    """Converts euros to dollars
    
    Args:
         parameters: currency in euros   
    
    Returns:
         currency in dollars
    """
    d = e * 1.21
    return d



def dollars_to_euros(d):
    """Converts dollars to euros
    
    Args:
         parameters: currency in dollars   
    
    Returns:
         currency in euros
    """
    d = d / euros_to_dollars(1)
    return d

def dollars_to_euros(dollars):
    """Converts dollars to euros
    
    Args:
         dollars: currency in dollars   
    
    Returns:
         currency in euros
    """
    euros = dollars / euros_to_dollars(1)
    return euros

def eastern_time_to_french(eastern):
    """Converts us eastern time to french time (military)
    
    Args:
         parameters: time in us eastern (military) as a string
    
    Returns:
         time in france (military) as a string
    """
    t = eastern.split(":")
    t[0] = (int(t[0]) + 6) % 24
    return str(t[0]) + ":" + str(t[1])




def celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit
    
    Args:
         parameters: temperature in celsius   
    
    Returns:
            temperature in fahrenheit
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to fahrenheit
    
    Args:
         parameters: temperature in fahrenheit   
    
    Returns:
            temperature in celsius
    """
    celsius = celsius_to_fahrenheit(celsius)
    return fahrenheit



def kilometers_to_miles(kilometers):
    """Converts kilometers to miles
    
    Args:
         parameters: distance in kilometers   
    
    Returns:
            distance in miles
    """
    miles = kilometers / 1.60934
    return miles


def liters_to_gallons(liters):
    """Converts liters to gallons
    
    Args:
         parameters: volume in liters  
    
    Returns:
            volume in gallons
    """
    gallons = liters / 3.78541
    return gallons


def mpg_from_metric(kilometers, liters):
    """Calculates miles per gallon
    
    Args:
         parameters: distance in kilometers
                     volume in liters
    
    Returns:
            miles per gallon
    """
    miles = kilometers_to_miles(kilometers)
    gallons = liters_to_gallons(liters)
    return miles / gallons

# TODO: Implement your functions that return here

# ---------------------- 
# Section 2: Functions that print
# ----------------------

def four_fours():
    """
    Express and print the values 0..9 using exactly four 4s.
    
    Allowed operators are +, -, *, //, %, **, and parentheses.
    
    Returns:
        None
    """
    print(4+4-4-4, "is 4+4-4-4")  # 0
    print(4-4+4//4, "is 4-4+4//4")  # 1
    print(4//4+4//4, "is 4//4+4//4")  # 2
    print((4+4+4)//4, "is (4+4+4)//4")  # 3
    print(4+(4-4)//4, "is (4+(4-4)//4)")  # 4
    print((4*4+4)//4, "is (4*4+4)//4")  # 5
    print(4+(4+4)//4, "is 4+(4+4)//4")  # 6
    print(4-(4//4)+4, "is 4-(4//4)+4")  # 7
    print(4+4+4-4, "is 4+4+4-4")  # 8
    print(4+4+4//4, "is 4+4+4//4")  # 9


def convert_from_seconds(seconds):     
    """
    Print number of days, hours, minutes, and seconds in a given number of seconds.
    
    Args:
        seconds: non-negative integer representing number of seconds
    
    Returns:
        None
    """
    days = seconds // (24 * 60 * 60) # Number of days
    seconds = seconds - days * (24 * 60 * 60) # Seconds remaining after days
    hours = seconds // (60 * 60)  # Number of hours
    seconds = seconds - hours * (60 * 60) # Seconds remaining after hours and days
    minutes = seconds // 60   # Number of minutes
    seconds = seconds - minutes * 60 # Seconds remaining after minutes, hours, and days

    print(days, "days")
    print(hours, "hours")
    print(minutes, "minutes")
    print(seconds, "seconds")
   
