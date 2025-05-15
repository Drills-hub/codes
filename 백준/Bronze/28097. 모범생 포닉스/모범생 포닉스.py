n= int(input())
t=list(map(int,input().split()))

d=(sum(t)+(n-1)*8)//24
h=(sum(t)+(n-1)*8)%24  

print(d,h)