#LINK:https://binarysearch.com/problems/Rotation-of-Another-String

#For reference: https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

#CODE:

class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1):
            return False
        t = s0 + s0
        if t.count(s1)>0:
            return True
        else:
            return False   
