import sys
input = sys.stdin.readline

n,m=map(int,input().split())
h=sorted(list(map(int,input().split())))

length=m
for i in h:
    if length>=i:
        length+=1
    else:
        break
print(length)