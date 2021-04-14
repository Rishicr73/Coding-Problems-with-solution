#### Topic :point_down:
![](https://img.shields.io/badge/-string-wheat)

#### Problem:point_down:
Given a list of positive integers nums, return the number of integers that have odd number of digits.

#### sample_Input:point_down:
```
nums = [1, 800, 2, 10, 3]
```
#### sample_output:point_down:
```
3
```
#### Solution[Python]:point_down:
```
class Solution:
    def solve(self, nums):
        s = 0
        for i in nums:
            if len(str(i)) % 2 != 0:
                s += 1
        return s      
```
#### solve Here:point_down:
[Binarysearch](https://binarysearch.com/problems/Odd-Number-of-Digits)
