#Given an array of positive integers.Find the leaders in an array
#NOTE : An element in an array is leader,if it is greater than or equal
# to all elements to its right side.Also the rightmost element is always a leader.

#Solution:
def leader(arr , n):
    max_ = arr[n-1]
    a = [arr[n-1]]
    
    for i in range(n-2, -1,-1):
        if arr[i] >= max_:
            a.append(arr[i])
            
            max_ = arr[i]
    for i in a:
        print(i , end = " ")   

arr = list(map(int , input().split()))    
leader(arr , len(arr))   

#Time complexity : O(n)
#Space complexity : O(1)


#company tag : Google
