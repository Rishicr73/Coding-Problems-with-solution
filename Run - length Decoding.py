#LINK : https://binarysearch.com/problems/Run-Length-Decoding


#CODE:

class Solution:
    def solve(self, s):
        decode = ''
        count = ''
        for i in s:
            if i.isdigit():
                count += i
            else:
                decode += i * int(count)
                count = ''
        return decode 
