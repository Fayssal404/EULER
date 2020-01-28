#!/usr/bin/python3.6m

"""Write a program that computes names scores in the file"""

import string
import time



#Search name in a list and get position
def get_position(names,name):
    """Search position of a name in sorted names"""
    return names.index(name) + 1


def value_of(name):
    """Compute numerical value of a string"""

    #Alphabetic letter
    letters = string.ascii_lowercase
    #Alphabetical value for each letter 
    letter_values = {letter:idx+1 for idx, letter in enumerate(letters)}

    name_value = 0
    for let in name:
        name_value += letter_values[let]
    
    return name_value


def main():
    """Multiply the alphabetical position in the list to obtain a name score, compute the total of all the name scores in the file"""


    names=open("names.txt","r").read().strip('""').split(",")
    names=[name.strip('""').lower() for name in names][:50]
    total_name_score = 0
        
    for name in names:
        position = get_position(names,name)
        nmrc_name = value_of(name)
        total_name_score += position*nmrc_name
    
    print("Names score in the file is {}".format(total_name_score))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print("Program run time {} seconds".format(end-start))






