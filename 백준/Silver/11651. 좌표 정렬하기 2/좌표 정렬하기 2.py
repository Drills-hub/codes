import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())

result = []
for _ in range(n):
    x,y=map(int, input().split())
    result.append([y,x])

result.sort()

for i in result:
    print(f"{i[1]} {i[0]}"+"\n")