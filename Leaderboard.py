nums = [40 , 80 , 40 , 70 ]
def solve(nums):
    if not(nums): #If length nums = 0 then return empty list(or num)
    
        return nums

    temp = [(n , i) for i , n in enumerate(nums)]   #store index and value as a tuple in a list
 
    temp.sort(reverse=True , key = lambda x : x[0]) #Sort it in reverse order according to values 
    #print(temp)
    rank = [0] * len(nums)
    rank[temp[0][1]] = 0
    r = 0
    #print(rank)
    for i in range(1 , len(temp)):
        if (temp[i][0] == temp[i - 1][0]):
            rank[temp[i][1]] = r
        else :
            r += 1
            rank[temp[i][1]] = r
    return rank 

print(solve(nums))       
#HERE IS ALINK OF QUESTION
#https://binarysearch.com/problems/Leaderboard
