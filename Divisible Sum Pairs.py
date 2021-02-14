#LInk : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(n-1):     #Here we have take upto n-1 becoz j = i+1 so just simplified it
        for j in range(i+1 , n):
            if (ar[i]+ar[j])%k == 0:
                c += 1
    return c           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
