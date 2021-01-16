def is_prime(n):
    if (n == 0 or n == 1):
        return False
    elif (n == 2 or n == 3)   :
        return True
    else :
        for i in range(2,n)  :
            if n % i == 0:
                return False   
        return True

def fib(n):
    l = [0,1]
    for i in range(2,n):
        l.append(l[i-1] + l[i-2])

    return l 
j = int(input())    
l = fib(j)
print(l)


sum_ = 0
for i in l:
    if i % 2 == 1:
        print(i)
        sum_ += i
print(sum_) 

sum_ = 0
for i in l:
    if i % 2 == 0:
        print(i)
        sum_ += i
print(sum_) 

sum_ = 0
for i in l:
    if (is_prime(i)):
        print(i)
        sum_ += i

print(sum_)        



   


       

        


    

        
      
            


            