#### Itertools.permutations():point_down:
```
permutations('ABCD', 2) : AB AC AD BA BC BD CA CB CD DA DB DC

```
```
Itertools.permutation() function falls under the Combinatoric Generators. The
recursive generators that are used to simplify combinatorial constructs such as
permutations, combinations, and Cartesian products are called combinatoric iterators.

As understood by the word “Permutation” it refers to all the possible
combinations in which a set or string can be ordered or arranged. Similarly here
itertool.permutations() method provides us with all the possible arrangements
that can be there for an iterator and all elements are assumed to be unique on
the basis of there position and not by there value or category. All these
permutations are provided in lexicographical order. The function
itertool.permutations() takes an iterator and ‘r’ (length of permutation needed)
as input and assumes ‘r’ as default length of iterator if not mentioned and returns all possible permutations of length ‘r’ each.

```

#### Question :point_down:

You are given a string S.
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

#### Example:point_down:
```
Input: HACK 2
output :
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
```
#### Python solution:point_down:
```
from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))

```
