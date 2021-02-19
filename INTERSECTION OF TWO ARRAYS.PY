QUE :: Given two arrays of integers arr1 and arr2 ,
create a function that returns an array that contains their
common elements(without duplicates)
Example : 
input : arr1 = [4,2,5,2,3,5]
        arr2 = [1,2,4,7,6,4,3]
output : [2 , 3, 4]

ans: 
#METHOD 1 IF ARRAY HAVE DUPLICate value

import time
arr1 = list(map(int , input().split()))
arr2 = list(map(int , input().split()))


start = time.time()
 
intersection_set = set(arr1).intersection(set(arr2))  #Here we just convert list into a set and use its formula = set1.intersection(set2)

intersection_lst = list(intersection_set)   
print(intersection_lst)

end = time.time()
print(f'finished in {round(end - start)} seconds')


#METHOD 2 WHEN ARR DONT HAVE DUPLICATE VALUE
import time
arr1 = list(map(int , input().split()))
arr2 = list(map(int , input().split()))


start = time.time()
l = []
for i in arr1:
  if i in arr2:
    l.append(i)
print(sorted(l))
end = time.time()
print(f'finished in {round(end - start)} seconds')
