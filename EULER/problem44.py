#!/usr/bin/python3.6m
#https://projecteuler.net/problem=44


def pentagone(n):
    return n*(3*n-1)//2

def whileiterptg(n_limit):
   """Return list of pentagone numbers for integer i <= n_limit""" 
   i=1
   pntgnList = []
   while i <= n_limit:
       pntgnList.append(pentagone(i))
       i +=1
   return pntgnList

pntgObj_1 = whileiterptg(10)  
def getPairs(pntgiterObj):
    """Get Pairs for all pentagone number in iter objects"""
    n = len(pntgiterObj)
    pairs = []
    #create pair of pentagone numbers, 
    for i in range(n):
        for j in range(1,n-i):
            pairs.append((pntgiterObj[i],pntgiterObj[i+j])) 

    return pairs

pairs = getPairs(pntgObj_1)        

def getSum(pairlist):
    """Compute the sum of pentagone pairs"""
    pairs_sum ={} 
    i = 0
    #Compute sum of pairs
    for pair in pairs:
        #Keep track of the sum value
        pairs_sum[str(i+1)] =pair[1]+pair[0]
        i +=1
    return pairs_sum    


#Identify pairs by sum values
suma = getSum(pairs)
def showsum(Sumvalue,pairsList):
    for i in Sumvalue.keys():
        print("Pair " + str(pairsList[int(i)]) + " sum to: " +str(Sumvalue[i])) 
#Compute difference of pairs

def getDiff(pairlist):
    """Compute the sum of pentagone pairs"""
    pairs_diff ={} 
    i = 0
    #Compute sum of pairs
    for pair in pairs:
        #Keep track of the sum value
        pairs_diff[str(i+1)] = abs(pair[1]-pair[0])
        i +=1
    return pairs_diff    




