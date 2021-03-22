#LINK ; https://binarysearch.com/problems/Strictly-Increasing-or-Strictly-Decreasing


#CODE:

class Solution:
    def solve(self, nums):
        
        if len(nums) != len(set(nums)):
            return False
        t = sorted(nums)    
        if nums == t or nums == t[::-1]:
            return True
        else:
            return False  
