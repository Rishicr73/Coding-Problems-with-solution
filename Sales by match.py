#LINK : https://www.hackerrank.com/challenges/sock-merchant/problem
#IN this question we have toh find how many pairs are there (pairs = two same integer is a one pair)

#CODE:
def sockMerchant(n, ar):
    pair = 0
    for i in set(ar):             #Here set() delete duplicate values
        pair += ar.count(i)//2    #Here we use count() to find how many times that integer come into that ar.
                                  #here we divide by 2 becoz we want how many pair can form by that integer(for.ex: 5//2 = 2 so there are 2 pair)
    return pair    
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
