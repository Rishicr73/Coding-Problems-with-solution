#LINK :  https://www.hackerrank.com/challenges/pairs/problem

#CODE :

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    i = 0
    j = 1
    c = 0
    while j < len(arr):
        d = arr[j] - arr[i]
        if d == k:
            c += 1
            j += 1
        elif d > k:
            i += 1
        else :
            j += 1
    return c               
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
#HERE WE USE A TWO POINTER APPROCH.    
