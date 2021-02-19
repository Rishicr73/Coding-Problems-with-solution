#QUE: Given two strings str1 and str2 made of lowercase letters
only, create a boolean function that checks if they're anagrams (made
of the same letters with the same number of occurrences)
example:
input: str1 = "listen"
       str2 = "silent"
output: true

#code:

import time                #Here we are just counting the time taken by the program to execute

str1 = input()
str2 = input()
start = time.time()
if sorted(str1) == sorted(str2):   
    print('true')
else:
    print('false')   

end = time.time()
print(f'finished in {round(end - start)} seconds')
