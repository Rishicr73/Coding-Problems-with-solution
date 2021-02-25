#LINK: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

#CODE:

num = 0
c = 0
while num > 0:
  if num % 2 == 0:
    num //= 2
  else:
    num -= 1
  c += 1
print(c)  
  
  
  
