#### Topic:point_down:
![](https://img.shields.io/badge/-array-wheat) 

#### Problem_point_down:
```
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
```
#### Example 1:point_down:
```
Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
```
#### Example 2:point_down:
```
Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.
```
#### Python:point_down:
```
class Solution:
    def sort012(self,arr,n):
        s1 = 0
        s2 = 0
        s3 = 0
        for i in range(n):
            if arr[i] == 0:
                s1 += 1
            elif arr[i] == 1:
                s2 += 1
            elif arr[i] == 2:
                s3 += 1
        i = 0
        while s1 > 0:
            arr[i] = 0
            i += 1
            s1 -= 1
        while s2 > 0:
            arr[i] = 1
            i += 1
            s2 -= 1
        while s3 > 0:
            arr[i] = 2
            i += 1
            s3 -= 1   
        return arr    
```
```
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
```
#### Approach:point_down:
```
1) Keep three counter c0 to count 0s, c1 to count 1s and c2 to count 2s
2) Traverse through the array and increase the count of c0 is the element is 0,increase the count of c1 is the element is 1 and increase the count of c2 is the element is 2
3) Now again traverse the array and replace first c0 elements with 0, next c1 elements with 1 and next c2 elements with 2.
```
