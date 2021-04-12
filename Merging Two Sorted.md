####Topic : point_down :

![](https://img.shields.io/badge/-string-wheat)
![](https://img.shields.io/badge/-two--pointer-wheat)

#### Problem :point_down:

Given two lists of integers a and b sorted in ascending order, merge them into one large sorted list.
#### Sample Input :point_down:
```
a = [5, 10, 15]
b = [3, 8, 9]
```
#### Sample  Output :point_down:
```
[3, 5, 8, 9, 10, 15]
```
#### Python :point_down:

```
class Solution:
    def solve(self, a, b):
        li, ri, result = 0, 0, []
        while li < len(a) and ri < len(b):
            if a[li] <= b[ri]:
                result.append(a[li])
                li += 1
            else:
                result.append(b[ri])
                ri += 1

        return result + a[li:] + b[ri:]    
```

#### Solve Here :point_down:
[binarysearch.com](https://binarysearch.com/problems/Merging-Two-Sorted-Lists)
