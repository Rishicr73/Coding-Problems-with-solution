#### itertools.combination() :point_down:
itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

#### Example:point_down:

```
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```

#### Question:point_down:
```
You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.
```
#### Input:point_down:
```
HACK 2
```
#### Output:point:down:
```
A
C
H
K
AC
AH
AK
CH
CK
HK
```
#### PY solution:point_down:
```
from itertools import combinations

s , n  = input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print(''.join(j))
```
