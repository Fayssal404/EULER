#!/usr/bin/python3.6m


""" Lattice paths program for n x n grid """



def lattice_paths(number):
    """ Number of lattice paths from (0,0) to (n,n) equal to C^n_{2n} """

    up_idx = list(range(1,2*number+1))
    low_idx = list(range(1,number+1))
    
    upper_index = up_idx[0]
    for i in up_idx[1:]:
        upper_index *= i
    
    lower_index = low_idx[0]
    for j in low_idx[1:]:
        lower_index *= j
    
    
    return upper_index//lower_index**2


def draw_square(width, height):
    """ Draw square number X number """
    for row in range(height + 1):
        if row in (0, height):
            print("*"* int(width+1))
        else:
            print("*" + "#"*int(width-1)+ "*")

#TODO: def draw_grid(number,number)


if __name__ == "__main__":
    print(lattice_paths(20))
    draw_square(2,2)

