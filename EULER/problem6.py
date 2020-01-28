#!/usr/bin/python3.6m



def square_sum(number):
    """Square sum numbers"""
    sum_ = number*(number+1)//2
    return sum_**2

def sum_square(number):
    """Sum squares numbers"""
    
    return (number+1)*(2*number+1)*number//6


def main():

    differ_ten = square_sum(10) - sum_square(10) 
    print(differ_ten)
    differ_hundred = square_sum(100) - sum_square(100) 
    print(differ_hundred)
    
if __name__ == "__main__":
    main()


