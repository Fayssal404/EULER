
""" Amicable numbers """

def proper_dividor(n):
    """ Numbers less than n which divide evenly into n"""
    return [ i for i in range(1,n) if n % i == 0]

def sum_(list):
    """ Sum element of a list """
    holder = 0
    for element in list:
        holder += element
    return holder    


def amical_pair(number):
    """ The Sum of proper divisor of number is equal, to the sum of the divisor of the sum of proper divisior of number"""

    #Sum proper divisor of number
    sum_divisor = sum_(proper_dividor(number))
    
    #Sum proper divisor of the sum proper divisor of number 
    sum_of_sum_divisor = sum_(proper_dividor(sum_divisor))

    if sum_of_sum_divisor == number and number != sum_divisor:
        return  (sum_divisor, number) 


def main():
    """ All the amicable numbers under 1000 """
    amical_numbers = [ amical_pair(n) for n in range(1,1000) ]     
    sum_amical = 0
    
    #Sum of amical numbers less then 1000
    for amical in amical_numbers:
        if amical != None:
            sum_amical += amical[1]+amical[0]
    return sum_amical

if __name__ == "__main__":

    dividor = proper_dividor(220)
    print(sum_(dividor))

    print(amical_pair(220))
    
    print("Sum of amical pairs less than {} is {}".format(1000,main()))
