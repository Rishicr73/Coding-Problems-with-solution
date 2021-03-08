#Link : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem



#CODE :

def jumpingOnClouds(c, k):
    e = 100
    f = 0
    
    for i in range(0 , n , k):
        
        f  +=  (1 + 2 * c[i])
    return(e - f)    
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
