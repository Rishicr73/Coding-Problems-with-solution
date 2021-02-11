#link :https://www.hackerrank.com/challenges/kangaroo/problem
#Little bit-logical 


def kangaroo(x1, v1, x2, v2):                      #Here is amthematical equation for understanding
    if v1 > v2 and (x2 - x1)%(v1 - v2)  == 0:      # [ (v1 * i)+x1 = v2*i+x2
                                                        x1 - x2 = (v2 * i) - (v2*i)
        return "YES"                                    x1 - x2 / v2 - v1 = i
                                                        here use a condition : x2 - x1 % v1 - v2 =0]
    else :
        return "NO"   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
