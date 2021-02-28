#Link: https://www.hackerrank.com/challenges/picking-numbers/problem

#Code:
#This question is some what tricky

def pickingNumbers(a):
    # Write your code here
    c = [0]*100
    for i in a:
        c[i] += 1
    max_ = 0    
    for i in range(1 , 100):
        max_ = max(max_, c[i] + c[i-1])
    return max_    
     #WE ned to select two adjacent numbers like(1 , 2 ) and return their count from array if there are more pair of adjacent number then we ned to select their maximum count.      
     #If not understood ask ajay sir .
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
    
