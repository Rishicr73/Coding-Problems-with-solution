#Link : https://www.hackerrank.com/challenges/sherlock-and-squares/problem
#CODE : #Easy

def squares(a, b):
    r = int(a**(1/2))
    p = int(b**(1/2))
    c = 0
    for i in range(r , p+1):
        if a <= i**2 <= b:
            c += 1
    return c        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
