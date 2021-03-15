#LINK : https://www.hackerrank.com/challenges/equality-in-a-array/problem

#CODE:

def equalizeArray(arr):
    l = []
    for i in list(set(arr)):
        t = arr.count(i)
        l.append(t)
    return(abs(max(l) - len(arr)))   
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
