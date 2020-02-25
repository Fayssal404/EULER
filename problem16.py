




def sumDigit(pow, num):
    """ Sum digit of number powered """
    
    sum = 0
    power = list(str(num**pow))

    for dig in power:
        sum += int(dig)
    
    return sum


if __name__ == '__main__':
    print(sumDigit(15,2))
