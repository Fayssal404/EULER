


def is_palindrom(number):
    """ Check a number if it is palindrom, read the same in reverse """
    listnum = list(str(number))
    n = len(listnum)
    
    if n % 2 == 0:
        return listnum[ : n // 2 ] == [ rev for rev in reversed(listnum[n//2: ]) ]
    else:
        return listnum[ : (n-1) // 2 ] == [ rev for rev in reversed(listnum[(n-1)//2 +1: ]) ]

def main():

    for i in range(100,1000):
        for j in range(100, 1000):
            if is_palindrom(i*j):
                print("{}, {}, palindrom {}".format(i,j, i*j))

if __name__ == "__main__":
    number = list(str(9009))
    print(number[:2])
    print([i for i in reversed(number[2:])])
    print(is_palindrom(9009))
    print(is_palindrom(9209))
    main()

