#!/usr/bin/python3.6m

import numpy as np
#multiples of 3 or 5 under 10 
def multiples(a,b,maxim):
    multiples =[i for i in range(1,maxim) if (i %a ==0) or (i%5 ==0)]
    return multiples, np.sum(multiples)

#sum element of a list
