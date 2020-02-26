#!/usr/bin/python3.6m




""" Fibonacci sequence, get Even numbers """


def fibonacci(n):
    """ Fibonacci Sequence """
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sumEven(max_value):
    """ Sum of fibonacci even valuees less then max value """
    sum = 0
    i = 0

    while (i <= max_value) and fibonacci(i) <= 1000:
        if fibonacci(i) % 2 == 0:
            sum += fibonacci(i)
        i += 1

    return sum

        
if __name__ == "__main__":
    print(sumEven(15))

