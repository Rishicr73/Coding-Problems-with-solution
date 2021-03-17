#LINK : https://www.hackerrank.com/challenges/minimum-distances/problem

#CODE:

def minimumDistances(a):
    l = []
    for i in range(len(a)):
        for j in range(i+1 , len(a)):
            if a[i] == a[j]:
                t = abs(i-j)
                l.append(t)
                break
    if bool(l) == True:   #EMPTY LIST HAS FALSE VALUE AND NON - EMPTY HAS TRUE(I.E B00L[NON-EMPTY LIST] == TRUE)       
        return(min(l))  
    else:
        return(-1)          
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
