#LINK : https://www.hackerrank.com/challenges/fair-rations/problem

#CODE:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#HINT :
#we have to convert all numberr into even and count how many number are changing during this process.
#Easy question

def fairRations(B):
    c = 0
    for i in range(len(B)-1):
        if B[i]%2 != 0:
            B[i] += 1
            B[i+1] += 1
            c += 2
    if B[-1]%2 != 0:
        return 'NO'
    else:
        return(str(c))   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
