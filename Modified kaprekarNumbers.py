#link : https://www.hackerrank.com/challenges/kaprekar-numbers/problem

#CODE:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    new=[]
    for k in range(p,q+1):
        num = str(k**2)
        d = len(str(k))        #number of digits
        r = num[-d:] 
        l = num[:-d]
        if not l:
            l='0'
        if int(r)+int(l) == k:
            new.append(k)
    if new:
        print(' '.join([str(k) for k in new]))
    else:
        print("INVALID RANGE")
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
    
    #IMPORTANT PART OF QUESTION:
    
    # The right hand part,r  must be d digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n .
