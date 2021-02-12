#Link :https://www.hackerrank.com/challenges/alternating-characters/problem?h_r=profile
#Hint in this you just need to find consecutive i.e for ex AA  if there is a consecutive pair that will deleted term so
#Simply calculate the consecative pair that will your answer

def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
