#!/usr/bin/python3.6m
#https://projecteuler.net/problem=50



#define isprime to check if it is a prime number 
print(7/2)
print(7//2)
print(7.0/2.0)
print(7.0//2.0)
print(7/2.0)
print(7//2.0)
print(7)
def isprime(prime):
    """Check if a number is prime number"""
    if prime >1:
        for i in range(2,prime):
            if (prime % i) == 0:
                return False  
                break
            else:
                return True
    else:
        return False
print(isprime(9))
#def getprime(n_prime):
#get list of all prime number before n_prime
#primelist = []
#for i in range(2,41):
#    if isprime(i):
#        primelist.append(i)
#print(primelist)
