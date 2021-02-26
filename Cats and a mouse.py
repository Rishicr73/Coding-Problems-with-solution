#Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#Really easy question 
def catAndMouse(x, y, z):
    r = abs(x-z)
    y = abs(y-z)
    if r < y:
        return('Cat A')
    elif y < r:
        return('Cat B')
    else:
        return('Mouse C')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
