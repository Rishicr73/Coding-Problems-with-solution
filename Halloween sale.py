#LINK : https://www.hackerrank.com/challenges/halloween-sale/problem

#CODE:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    g = 0
    while s >= 0:    
        s -= p
        p = max(p - d, m)   #HERE WE ARE TAKING MAX BETWEEN THEM BECAUSE AFTER M THERE VALUE IS SAME AS M (REFER EXAMPLE U WILL GET)
        g += 1
    return g - 1
       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
