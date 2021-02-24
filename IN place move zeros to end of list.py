#Link of the question : https://binarysearch.com/problems/In-Place-Move-Zeros-to-End-of-List
#CODE:

class Solution:
    def solve(self, nums):
        n = len(nums)
        s = [0]*len(nums)
        c = 0
        for i in range(n): 
            if nums[i] != 0:   
                s[c] = nums[i]
                c += 1
        return(s)  
