"""
CSCI150 Fall 2021 Lab 5

Name: Sujay Banerjee, Tucker Lamb
Section: A

Creativity:
Immplemented Q1, Q3, IQR to find statistical information for each quartile of the file.
Created range function to find the range of numbers in the data file.
Inserted mode function to find the mode of numbers in the data file.
"""

import math

"""
What is the name of the file? toystory.txt
File contained 2077 entries
Max: 5
Min: 1
Average: 4.146846413095811
Median: 4
Std. dev: 0.8521438720226554


What is the name of the file? jumanji.txt
File contained 701 entries
Max: 5
Min: 1
Average: 3.20114122681883
Median: 3
Std. dev: 0.9824705293126944

The first file contains data from movie ratings from 1-5 of the movie Toy Story and the second file contains ratings from 1-5 of Jumanji.
When analyzing the data for Toy Story, there were 2,077 reviews.
When analyzing the data for Jumanji, there were 701 reviews.
The average rating for Toy Story was around 4.15, so the majority of the people liked the movie a lot.
For Jumanji, the average rating was around 3.20, so not as liked as Toy Story.


What is the name of the file? 95income.txt
File contained 35326 entries
Max: 304998
Min: -13411
Average: 16974.277925607203
Median: 8929.5
Std. dev: 22838.45710389868

This file contains the income of surveyed participants from the Northeast region of the US from the 1995 census.
When analyzing the data, there were 35,326 participants. From this, the maximum income was $304,998 and the minimum was -$13,411 in debt.
The average income was around $16,974.

"""


def data_analysis():
    """
    Opens file and prints all statistical answers.
    
    Args: None
        
    Returns: None
    """
    filename = input("What is the name of the file? ")
    numbers = []
    with open(filename, "r") as data_file:
        for line in data_file:
            numbers.append(int(line.rstrip()))
            if len(numbers) == 0:
                return
    
    print("File contained", count(numbers), "entries")
    print("Max: ", int(max(numbers)))
    print("Min: ", int(min(numbers)))
    print("Average: ", average(numbers))
    print("Median: ", median(numbers))
    print("Std. dev: ", std_dev(numbers))
    print("Q1: ", Q1(numbers))
    print("Q3: ", Q3(numbers))
    print("IQR: ", IQR(numbers))
    print("Range: ", range_num(numbers))
    print("Mode: ", mode(numbers))

    
def count(numbers):
    """
    Counts total numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: Count
    """
    count = 0
    for line in numbers:
        count += 1
    return count
    

def average(numbers):
    """
    Finds average of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: average
    """
    avg = sum(numbers)/(count(numbers))
    return avg


def Q1(numbers):
    """
    Finds quartile 1 of  numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: quartile 1 of numbers
    """
    numbers.sort()
    half1 = len(numbers)/2
    mid1 = numbers[int(half1/2)]
    mid2 = numbers[int(half1/2-1)]
    if half1 % 2 == 0:
        return ((mid1+mid2)/2)
    else:
        return mid1
    

def median(numbers):
    """
    Finds median of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: median of numbers
    """
    numbers.sort()
    length = len(numbers)
    mid1 = numbers[int(length/2)]
    mid2 = numbers[int(length/2-1)]
    if length % 2 == 0:
        return ((mid1+mid2)/2)
    else:
        return mid1


def Q3(numbers):
    """
    Finds quartile 3 of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: quartile 3 of numbers
    """
    numbers.sort()
    num = numbers[(int(len(numbers)/2)+1):len(numbers)]
    half2 = len(num)
    mid1 = num[(int(half2/2))]
    mid2 = num[(int((half2/2)-1))]
    if half2 % 2 == 0:
        return ((mid1+mid2)/2)
    else:
        return mid1


def IQR(numbers):
    """
    Finds interquartile range of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: interquartile range of numbers
    """
    return int(Q3(numbers) - Q1(numbers))

        
def std_dev(numbers):
    """
    Finds standard deviation of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: standard deviations
    """
    variance = 0
    for line in numbers:
        variance += ((line - average(numbers))**2)/(count(numbers)-1)
    std = (variance)**0.5
    return std
        
    
def range_num(numbers):
    """
    Finds range of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: range
    """
    return max(numbers) - min(numbers)


def mode(numbers):
    """
    Finds mode of numbers in file.
    
    Args: numbers: List of numbers
        
    Returns: mode
    """
    numbers.sort()
    count = 0
    previous = numbers[0]
    new = 0
    for n in numbers:
        if n == previous:
            count += 1
            if count > new:
                new = count
                mode = str(n)
            else:
                count == new
                mode += ', ' + str(n)
        else:
            count = 1
        previous = n
    return mode


def frequencies(data):
    """
    Attempts to print the frequency of each item in the list data
    
    Args:
        data: List of "sortable" data items
    """
    data.sort()
    
    count = 0
    previous = data[0]

    print("data\tfrequency") # '\t' is the TAB character

    for d in data:
        if d == previous:
            # Same as the previous, increment the count for the run
            count += 1
        else:
            # We've found a different item so print out the old and reset the count
            print(str(previous) + "\t" + str(count))
            count = 1
        
        previous = d
    print(str(data[-1]) + "\t" + str(count))

# Do not remove this if statement, it is necessary to work with
# Gradescope
if __name__ == '__main__':
    # Invoke your data_analysis function when run with the green arrow
    data_analysis()