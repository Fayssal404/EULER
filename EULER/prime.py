
from math import sqrt



class Prime:

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

#Create a prime generator
    def next_prime(starting, end):
        """ Prime number generator """
        while starting <= end:
            if Prime.is_prime(starting):
                yield starting
            starting += 1

if __name__ == "__main__":

    sum = 0
    generator = Prime.next_prime(0, 10)
    while True:
        try:
            sum += next(generator)
        except StopIteration:
            break

    print(sum)

