### collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

#### Sample Code
```
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
```

#### Problem:point_down:
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N  number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu  earned.

#### Sample Input
```
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```
#### Sample Output
```
200
```
#### First solution:point_down:
```
With using Counter
from collections import Counter
x = int(input())
s = Counter(list(map(int , input().split())))
n = int(input())
income = 0
for i in range(n):
    si , xi = map(int , input().split())
    if s[si]: 
        income += xi
        s[si] -= 1

print(income)
```
#### Second solution:point_down:
```
without using counter
x = int(input())
v = list(map(int , input().split()))
d = {}
income = 0
for i in v:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
            
for i in range(int(input())):
    s , k = map(int , input().split())
    if s in d and d[s] > 0:
        
        income += k
        d[s] -= 1
print(income) 
```
#### Solve Here:point_down:
[Hackerrank](https://www.hackerrank.com/challenges/collections-counter/problem)
