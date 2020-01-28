

""" Problem 20: Factorial digit sum """ 




def factorial(n):
    """ Return factorial of n """
    if n < 0:
        print("Enter >0 integers.")
    elif n == 1:
        return 1
    else:
        return factorial(n-1)*n
    

def digitSum(n):
    """  Factorial digit sum """
    num = factorial(n)
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum


    


if __name__ == "__main__":
    number = 100
    print(factorial(number))
    print(digitSum(number))
