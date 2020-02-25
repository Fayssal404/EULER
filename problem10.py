#/usr/bin/python3.6m

import math
from random import randint, randrange



def get_primes(input_lists):
    """Get primes numbers from a list, not advised for long lists"""
    return [element for element in input_lists if is_prime(element)]

#When list is large that creating it will consume all the system memory
#Write a function that call get_primes with a start value and get all the primes larger than start
#we need a way to generate a value and, when asked for the next one, pick up where we left off


def get_primes_alt(number):

    #Make sure we never reach the end
    while True:
        if is_prime(number):
            yield number
        number +=1        

def solver_number_ten():
    """Get primes number from a starting point"""
    #Initial prime number
    total = 2
    for next_prime in get_primes_alt(3):
        #Add all primes less then 200
        if next_prime < 200:
            total += next_prime
        else:
            print(total)
            return 



def is_prime(number):
    """Check if a number is a prime number"""
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False

        for current in range(3, int(math.sqrt(number)+1), 2):
            if number % current == 0:
                return False
        return True

    return False
            
def main():
    """Run tests """
    numbers = [randrange(1,200) for _ in range(100)]
    print(get_primes(numbers))
    
if __name__ == "__main__":
    main()
    solver_number_ten()
