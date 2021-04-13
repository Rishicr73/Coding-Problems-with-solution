#### Topic :point_down:
![](https://img.shields.io/badge/-string-wheat)

#### Problem:point_down:

Given a lowercase alphabet string s, return the length of the longest substring with same characters.

#### Sample_Input:point_down:
```
s = "abbbba"
```
#### Sample_Output:point_down:
```
4
```
#### Python :

```
class Solution:
    def solve(self, s):
        if not s:
            return 0
        tot = 1
        size = 1
        for ix in range(1, len(s)):
            if s[ix] == s[ix - 1]:
                size += 1
            else:
                tot = max(tot, size)
                size = 1
        tot = max(tot, size)
        return tot
```
#### Time Complexity:point_down:
```
O(n) 
```
