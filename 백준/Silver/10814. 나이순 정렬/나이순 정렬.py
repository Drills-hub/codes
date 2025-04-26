import sys
input = sys.stdin.readline
print = sys.stdout.write

n=int(input())

result=[]
for i in range(n):
    x,y=input().split()
    x= int(x)
    result.append((x,i,y))

result.sort()

for i in result:
    print(f"{i[0]} {i[2]}"+"\n")