#Link: https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    return(min(p//2,n//2-p//2))   #simple question 
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
