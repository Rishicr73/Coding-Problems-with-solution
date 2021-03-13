#LINK : https://www.hackerrank.com/challenges/cut-the-sticks/problem

#CODE:

def cutTheSticks(arr):
    n = len(arr)
    s = sorted(list(set(arr))) #Here we want to sort set list to get correct order(i.e ascending or descending). if we directly sort the arr and then use set , in set there will not such order 
                               #it will go in random manner so that's why we have to sort the set of arr.
    l = []
    for i in s:
        l.append(n)
        n = n - arr.count(i)
    return l
       
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
