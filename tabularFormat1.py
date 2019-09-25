mystring = input()

ms1 = "".join([i for i in mystring if i not in "!@#$%^&*()><?."])

#ms2 = ms1.replace(' ','')
ms3 = ms1.split(" ")

#for take input from user and split from whitespace used split(" ")
maxlen = max(len(s) for s in ms3)
colwidth = maxlen + 3
#used for take # for bondry with maxlength + 3

print('#'*colwidth + "#")
#print ###### on top side
for s in ms3:
    print('# %-*.*s #' % (maxlen, maxlen, s))
    #side #### print using this 
print('#'*colwidth + "#")
#print ###### on bottom side
