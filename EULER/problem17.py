



#from 1 to 19 
BASE = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
BASE_dic = {str(digit+1): base for digit,base in enumerate(BASE[:-2])}

thirteen_nineteen = [ num + 'teen' for num in BASE[2:-3] ]  


ten_ninteen = {str(num): letter for num, letter in zip(range(10,20), BASE[-3:] + thirteen_nineteen)
        }


#from 20 to 99
twenty_nine = [BASE_dic[str(num)[0]] +'ty ' + BASE_dic[str(num)[1]] if str(num)[-1] != '0' else BASE_dic[str(num)[0]]+'ty' for num in range(20, 100)] 

twenty_ninenty = { str(u): ltnm for u, ltnm in zip(list(range(20,100)), twenty_nine)}
         
#from 100 to 99
one_nine_hundred = []

for num in range(100,1000):
    num_str = str(num)
    if num_str.endswith('00'):
        one_nine_hundred.append(BASE_dic[num_str[0]] + 'hundred ')
    
    elif not ( num_str.endswith('0', 1, 2) or num_str.endswith('1', 1, 2) ):
        one_nine_hundred.append(BASE_dic[num_str[0]] + 'hundred ' + twenty_ninenty[num_str[1:]])

    elif num_str.endswith('1', 1, 2):
        one_nine_hundred.append(BASE_dic[num_str[0]] + 'hundred ' + ten_ninteen[num_str[1:]])

    elif num_str.endswith('0', 1, 2):
        one_nine_hundred.append(BASE_dic[num_str[0]] + 'hundred ' + BASE_dic[num_str[2]] )
    

def main():
    """ If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? """
    num_lt = 0

    for i in range(1,100):
        if i<=9:
            num_lt += len(list(BASE_dic[str(i)]))
        elif i<=19:
            num_lt += len(list(ten_ninteen[str(i)]))
        elif i<=99:
            num_lt += len(list(twenty_ninenty[str(i)]))
        elif i<1000:
            num_lt += len(list(one_nine_hundred[str(i)]))
    
    print("Number of letters is %d" % num_lt)



if __name__ == '__main__':
    main()
