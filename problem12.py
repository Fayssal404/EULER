



def triangle(N):
    """ Compute triangle number """
    i = 0

    for j in range(1,N+1):
        i += j
    
    return i

#first 10 triangle terms
def rangetr(rn_tr):
    """ Compute range of triangular number """
    l1 = [triangle(num) for num in range(2,rn_tr+1)]
    
    return l1

def listdivisor(tr_num):
    """ List divisor of each triangular number """

    divisors = [div for div in range(1, tr_num+1) if tr_num % div == 0 ]

    return divisors

def main():
    """  What is the value of the first triangle number to have over five hundred divisors """

    i = 1
    while True:
        if len(listdivisor(triangle(i))) > 10:
                print("Triangular number {} of {} number has over than ten divisors".format(triangle(i), i))
                break
        i +=1

    



if __name__ == '__main__':
    print(triangle(7))
    print(rangetr(10))
    print(listdivisor(28))
    main()

