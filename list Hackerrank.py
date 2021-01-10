if __name__ == '__main__':
    N = int(input())
    l  = []
    for i in range(0,N):
        user_cmd = input().split()
        if user_cmd[0] == "insert":
            l.insert(int(user_cmd[1]),int(user_cmd[2]))
        elif user_cmd[0] == "remove":
            l.remove(int(user_cmd[1]))
        elif  user_cmd[0]  == "append" :
            l.append(int(user_cmd[1])) 
        elif user_cmd[0] ==  "sort" :
            l.sort() 
        elif user_cmd[0] == "reverse":
            l.reverse()
        elif user_cmd[0]  == "pop"  :
            l.pop()
        else :
            print(l)
        


    

        
    
    
   
   



