import re 
#import regularexpression 
def find_sum(str1): 
    # Regular Expression finds numeric values in between a string and do addition
    return sum(map(float,re.findall('\d+',str1)))

def avg(str1): 
    # Regular Expression that finds how many digits in string and find a average value  
    list(map(float,re.findall('\d+',str1)))
    ari = list(map(float,re.findall('\d+',str1)))
    return sum(ari)/len(ari)

str1 = input()
#for user input
print(find_sum(str1))
#prints additon value  
print(avg(str1))
#prints average value