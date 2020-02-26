


""" Lexicographic permutations """



def permute(lst):
    """ all permutation of a list """
    
    if len(lst) <= 1:
        yield lst
    else:
        for perm in permute(lst[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + lst[0:1] + perm[i:]



if __name__ == "__main__":
    l1 = list(range(10))
    pr = permute(l1)
    
    i = 1
    while i <=1000000:
        print("{}th permutation is {}".format(i, next(pr)))
        i +=1
