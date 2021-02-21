#Link: https://binarysearch.com/problems/Minimum-Cost-Sort

class Solution:
    def solve(self, a):
        b = sorted(a)    #Here we just sorted list in ascending 
        c = b[::-1]      #Here sorted list in descending 
        
        i = 0
        d = 0
        for n in range(len(a)):
            i += abs(b[n] - a[n])   #Here we are finding difference of sortd in ascending list with original and adding to i
            d += abs(c[n] - a[n])   #Here we are finding difference of sortd in descending list with original and adding to d
        return min(i , d)    
