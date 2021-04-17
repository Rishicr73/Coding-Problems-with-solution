#### Tpoic:point_down:
![](https://img.shields.io/badge/-binary--search-wheat)

#### Question:point_down:
Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).

#### Input:point_down:
```
x = 5
```
#### Output:point_down:
```
2
```
#### Explanation:point_down:
Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.

#### Algorithm:point_down:
```
1) Take care of some base cases, i.e when the given number is 0 or 1.
2) Create some variables, lowerbound l = 0, upperbound r = n, where n is the given number, mid and ans to store the answer.
3) Run a loop until l <= r , the search space vanishes
4) Check if the square of mid (mid = (l + r)/2 ) is less than or equal to n, If yes then search for a larger value in second half oF search space, i.e l = mid + 1, update ans = mid
5) Else if the square of mid is less than n then search for a smaller value in first half oF search space, i.e r = mid - 1
6) Print the value of answer ( ans)
```
#### Implementation:point_down:
```
class Solution:
    def floorSqrt(self, x):
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        
        while start <= end:
            mid = (start + end)//2
            if (mid * mid == x):
                return mid
            if (mid * mid < x)  :
                start = mid + 1
                ans = mid
            else:
                 
               end = mid - 1
        return ans
```
```
Time complexity: O(log n): 
The time complexity of binary search is O(log n).
Space Complexity: O(1): 
Constant extra space is needed.
```



