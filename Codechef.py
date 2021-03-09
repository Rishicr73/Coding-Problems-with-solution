#QUESTION : There are N seats in a row. You are given a string S with length N; for each valid i, the i-th character of S is '0' if the i-th seat is empty or '1' if there is someone sitting in that seat.Two people are friends if they are sitting next to each other. Two friends are always part of the same group of friends. Can you find the total number of groups?

#INPUT : 1)The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows
          #2) The first and only line of each test case contains a single string S.
#OUTPUT:
       #For each test case, print a single line containing one integer ― the number of groups.
  #CONSTRAINTS:
             #1≤T≤50
             #1≤N≤10
      
#EXAMPLE:
#INPUT: 4
      # 000
      # 010
      # 101
      # 01011011011110
#OUTPUT: 0
       # 1
       # 2
       # 4  
#Explanation: #Example case 1: Since all seats are empty, the number of groups is 0.
           #Example case 2: Since only one seat is occupied, the number of groups is 1.
           #Example case 3: Here, two seats are occupied, but since they are not adjacent, the people sitting on them belong to different groups.
           #Example case 4: Here, we have 4 groups of friends with size 1, 2, 2 and 4 respectively. That is, first group is sitting at 2nd seat, second group at 4th and 5th                                seat, third group at 7th and 8th seat and fourth group at 10th to 13th seat.
      
 #CODE :
for i in range(int(input())):
    s = input()
    c = 0
    if s[0] == '1':  #Here we are checking that its start from 1 then add 1 to c
        c += 1
    for i in range(1 , len(s)):
        if s[i] == '1' and s[i-1] != '1': #Here we are checking that if s[i] is same as s[i-1] so we didnt add becoz(11111 = 1 grp (read question))
            c += 1
    print(c)
      
      
      
      
