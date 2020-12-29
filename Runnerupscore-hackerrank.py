if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #here split function is used to  separate the given number by space
    #here we have take[:n] to keep upto that range(n)
    z = max(arr)
    #print(z)
    while max(arr) == z:
        arr.remove(max(arr))

print(max(arr))        
        
    
    
   
   



