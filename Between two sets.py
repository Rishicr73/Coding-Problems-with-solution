link: https://www.hackerrank.com/challenges/between-two-sets/problem

#In this question we have to find how many numbers are all factors of the 1 array and is a factor of all elements of the second array
#For ex [2 , 6] and [12 , 24 , 36] in 2 and 6 are all factors of 6  and 6 is also the factors of all element of second array .
#So we have to find how many numbers satisfies both the condition

code:
def getTotalX(a, b):
    maxA = max(a)
    minB = min(b)
    count = 0
    for i in range(maxA, minB+1): #Here we are taken this range from max(arr1) to min(array2) + 1 because in this range only we can get all nmbers which satisfies both the condition.
        if all([i%j==0 for j in a]):  #If it is true then only it will to further sets if false it stops .
        
            if all([j%i==0 for j in b]):
                count += 1
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
