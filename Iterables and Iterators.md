#### Theory:point_down:

The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their.
[documentation here](https://docs.python.org/2/library/itertools.html)

#### Problem:point_dow:
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1 -based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'

#### Example:point_down:
```
Sample Input

4 
a a c d
2
Sample Output

0.8333
```

#### Solution:point_down:
```
from itertools import combinations 

N = int(input())
S = raw_input().split(' ')
K = int(input())

num = 0
den = 0

for c in combinations(S,K):
    den+=1
    num+='a' in c
    
print float(num)/den
```
#### Solve Here:point_down:
[Hackkerrank](https://www.hackerrank.com/challenges/iterables-and-iterators/problem)

