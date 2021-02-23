#LINK OF THE QUESTION : https://www.hackerrank.com/challenges/two-strings/problem

#CODE :
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return('YES')
            break
    return('NO')    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
