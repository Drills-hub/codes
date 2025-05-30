import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    max_n = n
    if n==1:
        max_n = 1
    while n>1:
        if n%2==0:
            n=n//2
            max_n = max(max_n,n)
        else:
            n=n*3+1
            max_n = max(max_n,n)
    print(max_n)