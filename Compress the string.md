### itertools.groupby(iterable[, key])
```
1) Make an iterator that returns consecutive keys and groups from the iterable
2) The key is a function computing a key value for each element. If not specified or is None, key defaults to an identity function and returns the element unchanged.
3) Generally, the iterable needs to already be sorted on the same key function.
4)  It generates a break or new group every time the value of the key function changes (which is why it is usually necessary to have sorted the data using the same key functio
5)  for more info visit : https://docs.python.org/2/library/itertools.html#itertools.groupby
```
#### Question:point_down:
You are given a string S.Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

#### Example:point_down:
```
Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

```
#### Solution:point_down:
```
from itertools import groupby

for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")
```
#### Solve Here:point_down:
[www.hackerrank.com](https://www.hackerrank.com/challenges/compress-the-string/problem)
