#que: Given an array of integers arr ,
create a function that returns an array where
the element at index i is the sum :
arr[0]+arr[1]+...+arr[i]
EXAMPLE :
input: arr = [4,2,5,0,3,1]
output : [4,6,11,11,14,15]

code:
arr = list(map(int , input().split()))      
l = []
l.append(arr[0])
for i in range(1 , len(arr)):
    t = arr[i] + l[i-1]
    l.append(t)
print(l)  
