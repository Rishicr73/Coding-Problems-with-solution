n = int(input())
t = n
rev = 0
while t > 0:
    a = t % 10
    rev = rev * 10 + a
    t //= 10
 
print(rev)
if rev == n:
    print("It is a Palindrome Number")    
else :
    print("Not") 
       

