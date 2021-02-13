def theLoveLetterMystery(s):
    o = 0
    l = len(s)
    for i in range((l+1)//2):  #here we have taken this range upto l+1//2 becoz we want to go upto half of that string
        o += abs(ord(s[i]) - ord(s[l-i-1]))   #HERE just are find the ascii number of that character and then do operations with last items
    return o    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
    
    
    #link: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
