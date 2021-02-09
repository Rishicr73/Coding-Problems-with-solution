def miniMaxSum(arr):
    x = sum(arr)
    maxvalue = x - min(arr)    #Here we are only removing min(x) from len(s) so we can get max value
    minvalue = x - max(arr)    #same here also
    print(maxvalue , minvalue)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
    
    #link:https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=profile
