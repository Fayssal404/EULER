

import numpy as np 



def diag_sum(matrix):
    return np.sum([np.diag(matrix), np.diag(np.flip(matrix,0))])

if __name__ == '__main__':
    matrix = np.array([[21, 22, 23, 24, 25],
        [ 20, 7,  8,  9, 10],
        [ 19,  6,  1,  2, 11],
        [ 18,  5,  4,  3, 12],
        [17, 16, 15, 14, 13]])
    
    print(diag_sum(matrix))
