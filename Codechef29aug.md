#### Question
There are 3 problems in a contest namely A,B,C respectively. Alice bets Bob that problem C is the hardest while Bob says that problem B will be the hardest.

You are given three integers SA,SB,SC which denotes the number of successful submissions of the problems A,B,C respectively. It is guaranteed that each problem has a different number of submissions. Determine who wins the bet.

1) If Alice wins the bet (i.e. problem C is the hardest), then output Alice.

2) If Bob wins the bet (i.e. problem B is the hardest), then output Bob.

3) If no one wins the bet (i.e. problem A is the hardest), then output Draw.

Note: The hardest problem is the problem with the least number of successful submissions.

#### Input Format
* The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
* The first and only line of each test case contains three space-separated integers SA,SB,SC, denoting the number of successful submissions of problems A,B,C respectively.
#### Output Format
* For each test case, output the winner of the bet or print Draw in case no one wins the bet.

#### Solution :
```
def chef(Sa , Sb , Sc):
    if Sa < Sb and Sa < Sc:
        return("Draw")
    elif Sb < Sa and Sb < Sc:
        return("Bob")
    else:
        return("Alice")
    
t = int(input())
while t > 0:
    Sa , Sb , Sc = map(int , input().split())
    print(chef(Sa , Sb , Sc))
    t -= 1
    
```
#### This is easy question of codeshef starters (August 29)
