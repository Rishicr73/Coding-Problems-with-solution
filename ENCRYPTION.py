#1)
#FLOOR == It accepts a number with decimal as parameter and returns the integer which is smaller than the number itself.
#Syntax = math.floor(x)
#ex:print(math.floor(-21.6)) = -22
#Print(math.floor(14.6)) = 14

#2)
#CEIL == The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result  ,,
#Syntax = math.ceil(x)
#EX : print(math.ceil(5.3)) = 6
     #print(math.ceil(10.00)) = 10
     #print(math.ceil(-5.3)) = -5
     #print(math.ceil(22.6)) = 23
#SOURCE LINK : https://www.tutorialspoint.com/floor-and-ceil-function-python
      
#QUE)      
#Link :     https://www.hackerrank.com/challenges/encryption/problem

#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = len(s)
    r=math.floor(math.sqrt(len(s)))
    c=math.ceil(math.sqrt(len(s)))
    a = ''
    for i in range(c):
        a += s[i::c]+' '
    return a            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
      
      
      
