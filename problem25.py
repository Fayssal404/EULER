


"""Problem25: 1000-digit fibonacci number """


def fibonacci(idx):
    """ Fibonacci recursion version """
    if idx==2 or idx==1:
        return 1
    else:
        return fibonacci(idx-1) + fibonacci(idx-2)


def recdigit():
    """ 1000 digit fibo number Recursion version """
    fibo = 0
    i = 20 
    while True:
        fibo = fibonacci(i)
        print(fibo)
        if len(list(str(fibo))) == 5:
            print("Fibonacci number index is %d" % i)
            break
        else:
            i +=1
            continue

def fiboSpecial(n):
    """ Solving fibonacci using generating functions """

    return n//(1-n-n**2)

        

if __name__ == "__main__":
    #recdigit()
    print(fiboSpecial(3))
    
