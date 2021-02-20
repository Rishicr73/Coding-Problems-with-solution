link:
#https://www.hackerrank.com/challenges/anagram/problem

code:
import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    n = len(s)
    if n % 2 != 0:
        return(-1)
    else:
        t = s[:n//2]
        p = list(s[n//2:])
        ans = 0
        for i in t:
            if i in p:
                p.remove(i)
            else:
                ans += 1
    return ans                
               
                   
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
