# LINK : https://www.hackerrank.com/challenges/extra-long-factorials/problem
 #Code :
  
  def extraLongFactorials(n):
        if n <= 1:
            return 1
        return n * extraLongFactorials(n-1) #using recursion 
    
if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
