#LINK : https://www.hackerrank.com/challenges/acm-icpc-team/problem

#Code:

def acmTeam(topic):
    l = []
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            a = int(topic[i] , 2)   #here we converting a str for (i.e(str(101)) to 5) by giving base 2 for binary ,8 for octa , 16 for hexa
            b = int(topic[j] , 2)   #Here we convert it to int to perform 'OR' operation
            
            o = a | b                    
            l.append(bin(o).count('1'))  #Here we take bi to count the 1's in that o.
    m = max(l)
    x = l.count(m)       
    return(str(m),str(x)) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
