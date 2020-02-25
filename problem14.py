#!/usr/bin/python3.6m


""" Longest Collatz sequence """
import operator
import time

def Collatz(number):
    """ Generate Collatz sequence """
    collat_number = []
    while number != 1:
        if number %2 ==0:
            number = number//2
            collat_number.append(number)
        else:
            number = number*3 + 1
            collat_number.append(number)
    return collat_number


def main():
    """" Starting number under 100 produces the longest chain """
    starting = 13
    
    longest_chain = {}
    while starting < 10000:
        longest_chain[str(starting)] = len(Collatz(starting))
        starting +=1
    
    sorted_chain = sorted(longest_chain.items(), key=operator.itemgetter(1), reverse=True)
    print("Longest Collatz {} with {} items, under {}".format(*sorted_chain[0],starting))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Run time {} sec".format(end-start))

