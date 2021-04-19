#### Topic:point_down:
![](https://img.shields.io/badge/-array-wheat) 
![](https://img.shields.io/badge/-math-wheat)

#### Problem:point_down:
Given an array arr of integers of length N, the task is to find whether it’s possible to construct an integer using all the digits of these numbers such that it would be divisible by 3. If it is possible then print “1” and if not print “0”.

#### Example 1:point_down:
```
Input: N = 3
arr = {40, 50, 90}
Output: 1
Explaination: One such number is 405900.
```
#### Example 2:pont_down:
```
Input: N = 2
arr = {1, 4}
Output: 0
Explaination: The numbers we can form 
are 14 and 41. But neither of them are 
divisible by 3.
```
#### Python solution:point_dwon:
```
class Solution:
    def isPossible(self, N, arr):
        rem = 0
        for i in range(0,N):
            rem += arr[i]
        # code here
        if rem%3 == 0:
            return(1)
        else:
            return(0)
```
```
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
```
#### Approach:point_down:
```
So we simply find sum of array elements. If the sum is divisible by 3, our answer is Yes, else No.
```
