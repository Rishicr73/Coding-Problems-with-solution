link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#Basic question

def breakingRecords(scores):
    minimum = maximum = scores[0]
    min_ = max_ = 0
    for i in (scores[1:]):
        if i > maximum :
            maximum = i
            max_ += 1
        elif i < minimum:
            minimum = i
            min_ += 1  
    return(max_ , min_)          
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
