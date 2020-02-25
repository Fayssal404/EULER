#!/usr/bin/python3.6m



from math import sqrt


def pythagorean():
    
    b = 0
    c = 0
    s = 1000
    
    for a in range(1, s//3):
        for b in range(a, s//2):
            c = s - a - b

            if (a*a + b*b == c*c):
                return [a, b, c]


if __name__ == "__main__":
    print(pythagorean())

 
