

""" Distinct Powers """ 


def distinct_power(a,b):
    
    a_rge = list(range(2,a+1))
    b_rge = list(range(2, b+1))
    
    return { a**b for a in a_rge for b in b_rge}





if __name__ == '__main__':
    print(sorted(distinct_power(100,100)))

