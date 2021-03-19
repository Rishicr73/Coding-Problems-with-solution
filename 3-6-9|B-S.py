#LINK : https://binarysearch.com/problems/3-6-9

#CODE:

class Solution:
    def solve(self, n):
        l = [str(i) for i in range(1,n+1)]
        for i in range(len(l)):
            if int(l[i])%3 == 0:
                l[i] = 'clap'
            elif '3' in l[i]   :
                l[i] = 'clap'
            elif '6'in l[i]:
                l[i] = 'clap'
            elif '9' in l[i]:
                l[i] = 'clap'     
        return l  
