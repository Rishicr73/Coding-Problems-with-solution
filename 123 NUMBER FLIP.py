#LINK ; https://binarysearch.com/problems/123-Number-Flip

#FOR UNDERSTANDING : https://www.tutorialspoint.com/123-number-flip-in-python

#CODE: 

class Solution:
    def solve(self, n):
        l = list(str(n))
        for i in range(len(l)):
            if l[i] != '3':
                l[i] = '3'
                return int(''.join(l))
        return n
