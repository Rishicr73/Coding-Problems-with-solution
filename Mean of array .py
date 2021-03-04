#Link : https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

#Code: 

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        t = sorted(arr)
        r_p = int(0.05 * len(arr)) # so here there are telling to remove 5% i.e 0.05 of removing the smallest 5% and the largest 5% of the elements.
        new_list = t[r_p:len(arr)-r_p]  #So diretly multiple its and reove all 5% from starting and ending and add its in new_list find sum and len pf that new list
        mean = sum(new_list)/len(new_list)
        return mean
