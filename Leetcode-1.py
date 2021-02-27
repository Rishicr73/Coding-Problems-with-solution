#Que: Check If All 1's Are at Least Length K Places Away
#link:  https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

#Solution :
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l = []
        for i in range(len(nums)):
            if nums[i] != 0:
                l.append(i)
        for i in range(len(l)-1) :
            if l[i+1]-l[i] <= k:
                return False
        return True   
