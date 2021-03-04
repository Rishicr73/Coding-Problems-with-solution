#Link : https://www.hackerrank.com/challenges/permutation-equation/problem
#Code:

#Hint :
#p = [5,2,1,3,4]
#p[p[y]] = x
#p[y] = index(x)
#y = index(index(x))
#for x = 1
#p[p[y]] = 1
#p[y] = 3
#y = 4

def permutationEquation(p):
    l = []
    for i in range(1 , len(p)+1):
        t = p.index(i)+1  #Here we are adding one becoz index start from 0 and we have to take from indexing one so tht.
        s = p.index(t)+1
        l.append(s)
    return l        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
