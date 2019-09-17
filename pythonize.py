str = input("Enter a word: ")
#for input 

counter = 0
# counter variable to count the character in a string
for s in str:
      counter = counter+1
      n = counter
      #for last value of word use n 
      rs = str[1:n]
      crs = rs.capitalize()
      #crs store rs value as well as capitalize first letter
      rs2 = str[0]
      lrs = rs2.lower() 
      #lrs store rs2 value as well as lower the letter if its in CAPITALIZEFORM
      adpy = ("py")
      #this line use for add py at the end of every words

print( crs + lrs + adpy)
#for output