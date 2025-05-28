n=int(input())

for _ in range(n):
    count=0
    a,b=map(int,input().split())
    candy=list(map(int,input().split()))
    for i in candy:
        count+=i // b
    print(count)