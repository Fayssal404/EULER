#!/usr/bin/python3.6m

from math import sqrt

def is_prime(number):
    """Check if a number is a prime number"""

    if number > 1:
        if number==2:
            return True
        if number%2 ==0:
            return False
        for current in range(3,int(sqrt(number)+1),2):
            if number%current ==0:
                return False
        return True 
    return False

def main():
    i = 0 
    j = 0 
    while i < 10001 :

        if is_prime(j):
            i +=1
            print("{}th prime is {}".format(i,j))
        j+=1    

if __name__ == "__main__":
    main()
