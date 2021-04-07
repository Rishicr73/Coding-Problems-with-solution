#Link : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#Code:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    w = set()
    c = 1
    for i in range(len(s)):
        t = ord(s[i]) - 96    # they are given value of a = 1 then ascii of ord is 97 so we subtract from 96 all ascii alphabets we gets their weight according ques
        if (i+1 < len(s) and s[i+1] == s[i]):  #here we are count number of consecutive characters which are equal . if consecutive characters are not equal then we will 
                                               #will set its count as 1.
            c += 1
        else:
            c = 1
        w.add(t * c)         
    o = []
    for k in queries:
        if (k in w) :
            o.append('Yes')   
        else:
            o.append('No')          
    return o
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
