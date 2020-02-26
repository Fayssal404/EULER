#!/usr/bin/python3.6m


import random



def triangle(k):
    """ Generate triangle with k levels """
    trgle = []
    
    i = 1 
    while i < k:
        trgle.append(random.sample(range(1000), i))
        i += 1

    return trgle


def max_path_sum(triangle):        
    """ Maximum total from top to bottom and moving to adjacent numbers on the row below """
    
    max_sum = triangle[0][0] 
    

    for level, idx in zip(triangle[1:], range(0,len(triangle))):
            max_sum += level[idx]
    
    return max_sum





if __name__ == "__main__":

    text = [ [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


    triangle_one = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    print(max_path_sum(triangle_one))
    print("Solution is {}".format(max_path_sum(text)))
