


""" Non-abundant sums """


#Source: https://codereview.stackexchange.com/questions/39946/optimizing-solution-for-project-euler-problem-23-non-abundant-sums
def is_abundant(n):
    """ Perfect number of n less than n is deficient """
    i = 1
    sum = 0 
    
    for x in range(1, int(n/2) +1):
        if n % i == 0:
            sum += i
        i +=1
    return sum  > n           

""" All integers greater than 28123 can be written as the sum of two abundant numbers """

""" Find the sum of all the positive which cannot be written as the sum of two abundant numbers """

all_abundant = (x for x in range(1, 28123) if is_abundant(x))

def sum_abundant():
    """ Return sum of the abundant number under 28123 """
    sum = 0 
    for i in range(12, 28123):
        for abundant in all_abundant:
            if abundant >=i and is_abundant(i):
                sum += i 
    return sum





if __name__ == "__main__":
    print("Sum number cannot be written as abundant number is %d " % sum_abundant())
