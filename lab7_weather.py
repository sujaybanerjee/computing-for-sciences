"""
CS150 Lab 7


Name: Sujay Banerjee, Tucker Lamb
Section: A
Creativity:
Added functions get_town and find_town to extract the town from the url and return the town from the zip code.
Added get_field to extract any field from url and zipcode.
"""


import urllib.request
import ssl
import sys
ssl._create_default_https_context = ssl._create_unverified_context

TEST = "http://www.cs.middlebury.edu/~mlinderman/courses/cs150/f21/labs/lab7-test-data.json?zip=05753,us&APPID=9838b264525602b46f0b2ef8c191eef8&units=imperial"
REAL = "http://api.openweathermap.org/data/2.5/weather?zip=05753,us&APPID=9838b264525602b46f0b2ef8c191eef8&units=imperial"


def find_field(url, field):
    """Finds given field within the url for the zip code. Example for field: '"name":' 
        
        Args:
            url, field
        
        Returns:
            value for given field
    """
    with urllib.request.urlopen(url) as webpage:
        contents = webpage.read()
        contents = contents.decode("utf-8","ignore")
        start = contents.find(field)
        if start != -1:
             start += len(field)
             end = contents.find(",", start)
             value = contents[start:end].strip('"')
        return value


def get_field(zipcode, field):
    """Takes a string parameter representing a zipcode and string representing field
        
        Args:
            zipcode as string, field as string
        
        Returns:
            desired field value for zipcode

    """
    web = REAL.replace("05753", zipcode)
    return find_field(web, field)


# def find_temp(url):
#     """Finds temperature within the url for the zip code.
#         
#         Args:
#             url
#         
#         Returns:
#             Temperature at zip code
#     """
#     with urllib.request.urlopen(url) as webpage:
#         contents = webpage.read()
#         contents = contents.decode("utf-8","ignore")
#         start = contents.find('"temp":')
#         if start != -1:
#              start += len('"temp":')
#              end = contents.find(",", start)
#              temp = contents[start:end]
#         return temp

def get_temperature(zipcode):
    """Takes a string parameter representing a zipcode
        
        Args:
            zipcode as string
        
        Returns:
            temperature

    """
    web = REAL.replace("05753", zipcode)
    return float(find_field(web, '"temp":'))


# 
# def find_town(url, field):
#     """Finds the town within the url for the zip code.
#         
#         Args:
#             url
#         
#         Returns:
#             Town of zip code
#     """
#     with urllib.request.urlopen(url) as webpage:
#         contents = webpage.read()
#         contents = contents.decode("utf-8","ignore")
#         start = contents.find('"name":')
#         if start != -1:
#              start += len('"name":')
#              end = contents.find(",", start)
#              town = contents[start+1:end-1]
#         return town
    
    
def get_town(zipcode):
    """Takes a string parameter representing a zipcode
        
        Args:
            zipcode as string
        
        Returns:
            temperature

    """
    web = REAL.replace("05753", zipcode)
    return find_field(web,'"name":')



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python3 lab7_weather.py <zip_code>")
    else:
        print(get_temperature(sys.argv[1]))
        
        
    
    