text = input().split(" ")
#for take input from user and split from whitespace used split(" ")
maxlen = max(len(s) for s in text)
colwidth = maxlen + 3
#used for take # for bondry with maxlength + 3

print('#'*colwidth + "#")
#print ###### on top side
for s in text:
    print('# %-*.*s #' % (maxlen, maxlen, s))
    #side #### print using this 
print('#'*colwidth + "#")
#print ###### on bottom side