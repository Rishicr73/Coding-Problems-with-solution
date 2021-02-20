#SPLIT INTO CHUNKS OF K CHARACTERS

QUE: Given a string s and an integer k, create
     a funtion that splits it into chunks of k characters
     (the last chunk can contain less than k characters if
     necessary)
Example :
input : s = "Follow inside code"
         k = 4
output : ["Foll","ow i","nsid","e co","de"]

ANS:
s = input()
k = int(input())
l = []
for i in range(0 , len(s) , k):
    t = s[i:i+k]
    l.append(t)
print(l)   
