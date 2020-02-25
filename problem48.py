#!/usr/bin/python3.6m


""" Self powers """



def main():
    j = 0
    for i in range(1, 11):
        j += i**i
    
    print('Sum of self power is %d ' % j) 

if __name__ == '__main__':
    main()


