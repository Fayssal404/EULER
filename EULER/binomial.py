#!/usr/bin/python3.6m 


class BinomialCoeff():
    def __init__(self,upper_index,lower_index):
        self.upper_index = upper_index
        self.lower_index = lower_index


    def factorial(self):
        """the permutation of n distinct objects there are: n!"""
        #No combinatorial interpretation for real number in lower_index        
        if self.lower_index < 0:
            return 0
        elif self.upper_index == 0:
            return 1
        else:
            nmbrs = list(range(1,self.upper_index+1))
            res = nmbrs[0]
            for number in nmbrs[1:]:
                res *= number
        return res

    def symmetry(self):
        """Symmetry identity"""
        if self.lower_index < 0:
            return 0
        elif self.upper_index == 0:
            return 1
        else:
            nmbrs = list(range(1,self.upper_index-self.lower_index))
            sym = nmbrs[0]
            for number in nmbrs[1:]:
                sym *= number
        return sym        

    def combiCoeff(self):
        """the number of possibility to choose lower_index from upper_index balls"""
        if self.lower_index < 0:
            return 0
        elif self.upper_index < self.lower_index:
            return 0
        else:
            coeff =factorial(self.upper_index)/factorial(self.lower_index)*factorial(self.upper_index-self.lower_index)
            return coeff

bino = BinomialCoeff(4,2)
print(bino.combiCoeff())
