#Hackerrank 
#Link : https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product
K, M = map(int,input().split())
def Sq(n):
    return int(n)**2
List = []
for i in range(K):
    List.append(list(map(Sq,input().split()[1:])))
print(List) 

Max=0    
for T in product(*List):
    print(T)
    Sum=sum(T)%M
    if Sum>Max:   #finding maximum sum out of all tuples
        Max=Sum
print(Max)

#SIMPLE QUESTION - Easy

#POINTS TO REMEMNBER :
1) ITERTOOLS.PRODUCT()
2 ) IN lINE NO 10 WE HAVE Taken [1:] BECAUSE WE HAVE GIVEN how many numbers are there in first position
