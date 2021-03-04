#Link : https://leetcode.com/problems/thousand-separator/

#Code :

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n))<= 3:
            return(str(n))
        else:
            n = str(n)[::-1]
            return '.'.join((n[i:i+3] for i in range(0 , len(n) , 3)))[::-1]
