#LINK : https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    x=sum(bill)-bill[k]

    if x/2==b:

        print('Bon Appetit')

    else:

        print(b-(x//2))
    
    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)  #HERE DIREST FUNCTION IS CALLING SO USE(PRINT STATEMENT IN FUNCTION)
                             #If its has val = function() use return function 
