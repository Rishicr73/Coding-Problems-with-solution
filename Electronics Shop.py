#link : https://www.hackerrank.com/challenges/electronics-shop/problem

#method 1:

def getMoneySpent(keyboards, drives, b):
    l = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j]<= b:
                l = max(l , (keyboards[i]+drives[j]))
    return l               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
    
    #Method 2:
    def getMoneySpent(keyboards, drives, b):
    l = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j]<= b:
                l.append(keyboards[i]+drives[j])
    if not l:
        return(-1)  
    else:
        return(max(l)) 
     #method 3:
    #OR in this u can directly check that if min(1starr) and min(2ndarr) addition is not less that d then diretlt return -1

