#Link : https://www.hackerrank.com/challenges/migratory-birds/problem

#CODE:
def migratoryBirds(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i , 0)+1  #Here we are counting how many time one number occurs
    m = max(d.values())  #Then here we are finding max value of (d)
    l = []               #Here we are taki\en a list
    for i in d:
        if d[i] == m:    
            l.append(i)
    return(min(l))    

       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
