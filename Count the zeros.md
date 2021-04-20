#### Question 👇
Given an array of size N consisting of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.
#### Example:point_down:
```
Input:
N = 12
Arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}
Output: 3
Explanation: There are 3 0's in the given array.
```
#### Python solution 👇

```
class Solution:
    def countZeroes(self, arr, n):
        # code here
        c  = 0 
        for i in arr :
            if i == 0:
                c += 1
        return c        
```
```
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
```
