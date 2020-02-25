#!/usr/bin/python3.6m 

#://projecteuler.net/problem=42



import numpy as np
import math
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import regex

def triangular(n):
    """Triangular number forumula"""
    return n*(n+1)//2

def istriangular(tr):
    """Check if a number is triangular"""
    n1 = (-1 +  math.sqrt(1+8*tr))//2
    if tr == triangular(n1):
        return True
    else:
        return False

#convert each letter in a word to a number corresponding to its alphabetical order
alphabet = "abcdefghijklmnopqrstuvwxyz"
#map every letter to its number 
number = list(range(1,len(alphabet)+1))
mapped = {u: v for u,v in zip(list(alphabet), number)}

def convertion(string):
    """Convert a string into sequence of positional numbers
    return a list of alphabetical position
    """
    string = list(string)
    convertion = []
    for s in string:
       convertion.append(mapped[s]) 
    return convertion   

"""
Exemple 1:
    
STRING = input("Enter a string: ")
fayssal # "fayssal" is assigned to STRING name

TRGLR = np.sum(convertion(STRING))

if istriangular(TRGLR):
    print(STRING + " is a triangular word.")
else:
    print(STRING + " isn't triangular word.")
"""

#read and transforme it to minuscule letter
html = urlopen("https://projecteuler.net/project/resources/p042_words.txt")
bs4Obj = BeautifulSoup(html)

#Find first paragraph tag, get text
paragraph = bs4Obj.find("p").get_text()
#split string 
paragraphs = list(paragraph.split(","))
#store name and strip trailing and leading "
variables = []
for variable in paragraphs:
    variables.append(str(variable).strip('""').lower())

for i in variables:
    TRGLR = np.sum(convertion(i))
    if istriangular(TRGLR):
        print("-"*80 )
        print( i + " is Triangular word!!" )
        










