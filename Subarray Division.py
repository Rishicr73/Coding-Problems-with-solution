#link: https://www.hackerrank.com/challenges/the-birthday-bar/problem

code:
def birthday(s, d, m):
    sum_ = 0
    for i in range(n):
        t = sum(s[i:i+m])
        if t == d:
            sum_ += 1
    return sum_        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
