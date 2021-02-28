#Link:https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    if max(height)<k:    #In this question u only need to find how many dose it required to claer all so max(value) of that - k
        return 0
    else:    
        return(max(height)-k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
