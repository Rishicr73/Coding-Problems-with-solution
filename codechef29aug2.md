#### Question :
Chef has an array A containing N integers. The integers of the array can be positive, negative, or even zero.

Chef allows you to choose at most K elements of the array and multiply them by −1.

Find the maximum sum of a subsequence you can obtain if you choose the elements of the subsequence optimally.

Note: A sequence a is a subsequence of a sequence b if a can be obtained from b by deletion of several (possibly, zero or all) elements. For example, [3,1] is a subsequence of [3,2,1] and [4,3,1], but not a subsequence of [1,3,3,7] and [3,10,4]. Note that empty sequence is also a subsequence.

#### Input Format
* The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
* The first line of each test case contains two space-separated integers N,K.
* The second line of each test case contains N space-separated integers A1,A2,...,AN

#### Output Format
For each test case, print a single line containing one integer - the maximum sum of a subsequence you can obtain.

#### Solution :
```
t = int(input())
while t > 0:
    n , k = map(int , input().split())
    l = list(map(int , input().split()))
    l.sort()
    for i in range(k):
        if (l[i]) < 0:
            l[i] = l[i] * (-1)
    ans = 0
    for i in range(n):
        if(l[i] > 0):
            ans += l[i]
    print(ans)
    t -= 1
```

