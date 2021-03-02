#Link : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#Code


def beautifulDays(i, j, k):
    c = 0
    for i in range(i , j+1):
        t = str(i)
        p = t[::-1]
        if abs(int(t)-int(p))%k == 0:
            c += 1
    return c        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
