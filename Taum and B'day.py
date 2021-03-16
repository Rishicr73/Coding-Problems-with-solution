#LINK : https://www.hackerrank.com/challenges/taum-and-bday/problem

#CODE :

def taumBday(b, w, bc, wc, z):
    # Write your code here
    return((b*min(bc , wc+z))+w*min(wc , bc+z))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
    
    #EDITORIAL:
    #https://www.hackerrank.com/challenges/taum-and-bday/editorial
    
    #The problem can be easily solved with the fact that there will be only three cases.
    #1)  Tau buys b black and w  white gifts (b*bc)+(w*wc) = cost.
    #2) Tau buys all black gifts and converts w gifts to white. (b+w)*bc+w*z.
    #3)  Tau buys all white gifts and converts b gifts to black. (b+w)*wc+b*c.
    #We can take all three cases one by one, and the case that costs the least will be the answer. See setter's code for clear implementation.
    
    
   #The above logic can be proved using the fact that, if the minimum is any case other than first one, if he is buying more than b
    #black gifts, then he will prefer to buy all black. The same thing applies to white as well.
    
    #Code :
   # print min(b * bc + w * wc, bc * (b + w) + w * z, wc * (b + w) + b * z)
