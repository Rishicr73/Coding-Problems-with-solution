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
        
#Intuition
#Here is the easy approach

#One way is to find the exact pivot point where the string is assumed to be rotated. However this might not work on all testcases.
#An easier way is : Given s0 and s1, every possible rotation of s0 is contained in s0+s0. Why?

#assume -> s='abc'
#abc is one rotation of s
#We know that bca is one rotation. In the original string we can see bc is there. So only 'a' is not there. Lets add a. So now bca is there in s, s =abca
#We know that cab is one rotation. In original stringconly is there. So 'ab' is not there. Lets add ab. So now cab is there in s. s=abcab
#If you notice the last string every rotation is covered. abc,bca,cab. Of course s0+s0->abcabc (extra a) but writing s0+s0 is simpler.
#This is the logic. Please work it out to see that s0+s0 contains all rotations of s0       
