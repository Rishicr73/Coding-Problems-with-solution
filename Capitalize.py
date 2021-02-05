s = input()
n = s[0].upper()
for i in range(1 , len(s)):
  if (s[i - 1] == ' '): #Here we have find space using slicing in s
    n += s[i].upper()   #After finding space we use uppercase to captialise a letter after space
  else:
  n += s[i]     #here we have adding the elements which has no space between there elements
print(n)


#link of the question https://www.hackerrank.com/challenges/capitalize/problem?h_r=profile
