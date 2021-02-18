#The Fibonacci sequence is defined as follows:
Uo = 0
U1 = 1
Un = Un-1 + Un-2
Given a positive integer n , create a
function that returns the value of Un.
EXAMPLE:
input: 6
output : 8
explanation :
Uo = 0 , U1 = 1 , U2 = 1 , U3=2 , U4 = 3,U5 = 5 , U6 = 8

#CODE:
l = [0 , 1]  
for i in range(2 , int(input())+1):
    t = l[i-2] + l[i-1]
    l.append(t)
print(t)  
