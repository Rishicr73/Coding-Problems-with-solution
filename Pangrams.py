#link : https://www.hackerrank.com/challenges/pangrams/problem

#code:
# Complete the pangrams function below.
def pangrams(s):
    s=set(s.lower())
    if len(s)==27:
        return 'pangram'
    else:
        return 'not pangram'
    #here 26 alphabets and addtion of one for space
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
