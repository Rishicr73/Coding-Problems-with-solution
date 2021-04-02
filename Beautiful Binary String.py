#LINK : https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#CODE :

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    t = '010'
    v = b.count(t) 
    return(v)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    #CONFUSING PART : b = '0101010' = u think that here is 3 substring of 010 but only two this is beacuse if we start from first 
    #there is 010 and after that the number is 101 so it is not substring then it will go next number after 1 that is 0 and we get 010 
    #it is substring ..so in this question we have to find how many substring are there.
