#very very simple question link : https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_a = 0
    count_o = 0
    for i in apples: #(here just we are taking a each value from apples so we could check by adding to a its in that range (i.e = s ,t) if it is there we add one to it)
        if  s <= a + int(i) <= t:
            count_a += 1
    print(count_a)
    for j in oranges :#(same here as we have taken in apples)
        if s <= b + int(j) <= t:
            count_o += 1
    print(count_o)        
        
    

if __name__ == '__main__':
    st = input().split()   #don,t confuse here this are given in question otherwise read step by step u can understood what they are.

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
