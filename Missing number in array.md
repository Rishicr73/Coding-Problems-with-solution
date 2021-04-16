#### Question:point_down:
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

#### Example 1:point_down:
```
Input:
N = 5
A[] = {1,2,3,5}
Output: 4
```
#### Your Task:point_down:
You don't need to read input or print anything. Complete the function MissingNumber() that takes array and N as input  parameters and returns the value of the missing number.

```
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
```

#### Approach:point_down:
```
The length of the array is n-1. So the sum of all n elements, i.e sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. Now find the sum of all the elements in the array and subtract it from the sum of first n natural numbers, it will be the value of the missing element.
```
#### Algorithm:point_down:
1) Calculate the sum of first n natural numbers as sumtotal= n*(n+1)/2
2) Create a variable sum to store the sum of array elements.
3) Traverse the array from start to end.
4) Update the value of sum as sum = sum + array[i]
5) Print the missing number as sumtotal - sum
#### Python:point_down:
```
class Solution:
    def MissingNumber(self,array,n):
        s = sum(array)
        t = 0
        for i in range(1,n+1):
            t += i
        return(t-s)   
```
#### Solve:point_down:
[geeksforgeeks.org](https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1#)
