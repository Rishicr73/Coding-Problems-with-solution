#Link : https://www.hackerrank.com/challenges/chocolate-feast/problem

#Code:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    n=n//c    #Total chocolates
    wrap=n     #Wrappers
    while(wrap>=m):
        k=wrap//m    #WRAPPERS TO CHOCALATE
        n+=k          
        wrap=k+(wrap%m)  #REMAINING WRAPPER
    return(n)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
