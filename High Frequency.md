#### Topics :point_down:
![](https://img.shields.io/badge/-hash--map-wheat)

#### Problem :point_down:
Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.

#### Sample Input :point_down:
nums = [1, 4, 1, 7, 1, 7, 1, 1]

#### Sample Output :point_down:
 5
 
<details>
<summary>Expand</summary>
#### Python :point_down:
```py
  class Solution:
    def solve(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        maxi = 0
        for key in d:
            maxi = max(maxi, d[key])
        return(maxi) 
```
#### Python :point_down:
```py
  class Solution:
    def solve(self, nums):
        if nums == []:
            return 0
        t = set(nums)
        l= []
        for i in t:
            s = nums.count(i)
            l.append(s)
        return max(l)   
```  
</details>

#### Solve Here :point_down:
[binarysearch.com](https://binarysearch.com/problems/High-Frequency)
  
  
