#Link : https://binarysearch.com/problems/Run-Length-Encoding

#Code:
class Solution:
    def solve(self, s):
        c = 1
        p = ''
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                p += str(c)+s[i-1]  
                c = 1
        p += str(c) + s[-1]  #Here this for last element which do not count in that if and else condition 
        return p    
