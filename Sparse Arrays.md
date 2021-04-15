#### Topic:point_down:
![](https://img.shields.io/badge/-array-wheat) 

#### Question:point_down:
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
#### Example:point_down:
```
Strings = ['ab','ab','abc'] 
queries = ['ab','abc',bc']
```
There are 2 instances of 'ab', 1 instance of 'abc' and 0 instance of 'bc'.For each query, add an element to the return array, result = [2,1,0]

#### Python:point_down:
```
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    d = {}
    w = []
    for i in strings:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for j in queries:
        if j in d :
            w.append(d[j])
        else:
            w.append(0)    
    return w        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
```
#### Solve Here:point_down:
[Hackerrank.com](https://www.hackerrank.com/challenges/sparse-arrays/problem)

#### Time complexity:point_down:
```
O(N*Q*20)
```
