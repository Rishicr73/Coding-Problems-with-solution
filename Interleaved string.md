#### Topics :point_down:
![](https://img.shields.io/badge/-string-wheat)


#### Problem :point_down:

Given two strings s0 and s1, return the two strings interleaved, starting with s0. If there are leftover characters in a string they should be added to the end.
#### Sample Input :point_down:
```
s0 = "abc"
s1 = "xyz"
```
#### Sample Output :point_down:
```
"axbycz"
```
#### Python :point_down:

```
class Solution:
    def solve(self, s0, s1):
        res = ""
        i = 0
        j = min(len(s0) , len(s1))
        while i<j:
            res += s0[i]+s1[i]
            i += 1
        return res + s0[i:]+s1[i:] 
```
#### Solve Here :point_down:
[binarysearch.com](https://binarysearch.com/problems/Interleaved-String)
