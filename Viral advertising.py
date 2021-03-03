#Link : https://www.hackerrank.com/challenges/strange-advertising/problem
#Hint : Do not confuse with  floor
#WE give shared = 5 becoz in staring company only share to five people.
#And half of that five people like the ads and each share to three people


#Code :

def viralAdvertising(n):
    shared=5
    cumulative=0
    for d in range(0,n):
        liked=shared//2
        shared=liked*3
        cumulative=cumulative+liked
    return cumulative
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
