link: https://leetcode.com/problems/n-th-tribonacci-number/

code:
n = int(input())
l = [0,1,1]
for i in range(3 , n+1):
    t = l[i-1]+l[i-2]+l[i-3]
    l.append(t)
print(l[n])    
