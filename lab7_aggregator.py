"""
Gets the temperature data and aggregates it into a file

CS150 Lab 7

Name: Sujay Banerjee, Tucker Lamb
Section: A
Creativity:
Added zipcode to check_file function and wrote it into the file.
Inserted if statement to check to see if a valid zip code was entered.
"""

import os
import sys
import lab7_weather
import datetime

def check_file(filename, date, hour, temperature, zipcode):
    """Checks file to see if it already exists on the computer.
        
        Args:
            filename, date, hour, temperature, zipcode
        
        Returns:
            True or False
    """
    with open(filename, "r") as file:
        for line in filename:
            if line.startswith(date + "," + hour + "," + temperature + "," + zipcode):
                return True
        return False

def get_hour():
    """Gets the hour of the day in military time
        
        Args:
            none
        
        Returns:
            hour
    """
    now = datetime.datetime.now()
    return str(now.hour)
   
def get_date():
    """Gets date of the day
        
        Args:
            none
        
        Returns:
            date
    """
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python3 lab7_aggregator.py <file> <zip_code>")
    else:
        file = sys.argv[1]
        zipcode = str(sys.argv[2])
        date = str(get_date())
        hour = str(get_hour())
        temperature = str(lab7_weather.get_temperature(zipcode))
        if len(zipcode) != 5:
            print("Enter a valid zipcode.")
        if os.path.exists(file):
            if check_file(file, date, hour, temperature, zipcode) is False:
                info = (date + "," + hour + "," + temperature + zipcode)
                with open(file, "a") as data_file:
                    data_file.write(info)
        else:
            info = (date + "," + hour + "," + temperature + zipcode)
            with open(file, "a") as data_file:
                data_file.write(info)
