N=int(input())
a,b=map(int,input().split())

count=0
count+=a//2
count+=b

if count<N:
    print(count)
else:
    print(N )