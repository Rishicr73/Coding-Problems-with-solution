link : https://binarysearch.com/problems/Max-Product-of-Three-Numbers

#First method 
class Solution:
    def solve(self, nums):
        nums.sort()
        return(max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3]))
        
#Second method
nums = list(map(int , input().split())
t = sorted(nums)
l = []
for i in range(len(nums)):
  for j in range(i+1 , len(nums)):
      for k in range(j+1 , len(nums)):
        y = nums[i]*nums[j]"*nums[k]
        l.append(y)
print(max(l))        
