


from prime import Prime


""" Distinct prime factor """
""" find the first four consecutive integers to have four distinct prime factors each """


def primeFactor(n):
    """ Return a list of prime factors """
    consecutive = []
    i = 2
    while i <= n:
        while n % i == 0:
            n = n // i
            consecutive.append(i)
        i +=1
    return consecutive
                

def main():

    fourconsec = []
    
    j = 20
    while len(fourconsec) <= 4:
        factors = primeFactor(j)
        if len(set(factors)) == 4:
            fourconsec.append((j, factors))
        j+=2
    print(fourconsec)

if __name__ == "__main__":
    n1 = 644
    print(primeFactor(n1))

    main()
            
    




