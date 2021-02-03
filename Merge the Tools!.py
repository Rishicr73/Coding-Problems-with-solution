def merge_the_tools(string, k):
    
    for i in range(0 , len(string) , k): #Here we have taken this range i.e (o , len(string) , k) is because we take k step ahead 
        Str = string[i:i+k]   #here we do slicing
        s = ''                #Here is empty string
        for n in Str:
            if n not in s:    
                s += n
        print(s)        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
#link of the question 
# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=profile
