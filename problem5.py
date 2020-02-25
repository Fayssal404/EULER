#!/usr/bin/python3.6m


""" Smallest multiple """



def smallest_mult_in(end_range):
    """ Smallest multiple for number in range 'end_range' """
    
    starter = end_range

    while True:
        #Check divisibility by all number in range
        if all(starter % num == 0 for num in range(1,end_range+1)):
            return starter
        else:
            starter += 1


if __name__ == "__main__":
    print("Smallest number divisible by all the number from 1-10 is {}".format(smallest_mult_in(10)))
    print("Smallest number divisible by all the number from 1-20 is {}".format(smallest_mult_in(20)))
            
