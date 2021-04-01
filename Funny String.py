#LINK : https://www.hackerrank.com/challenges/funny-string/problem

#I HAVE MADE HERE TWO   EASY SUBMISSION

#CODE:
#[1ST SUBMISSION]
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return('Not Funny')
    return('Funny')    
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
    
 #[2ND   SUBMISSION]
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    l = [] 
    for i in s:
        l.append(ord(i))
    t = l[::-1] 
    p = []   
    for i in range(1 , len(l)):
        s = abs(l[i]-l[i-1])
        p.append(s)
    u = []
    for i in range(1,len(t)):
        f = abs(t[i] - t[i-1])
        u.append(f)
    if u == p:
        return('Funny')
    else:
        return('Not Funny')    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
