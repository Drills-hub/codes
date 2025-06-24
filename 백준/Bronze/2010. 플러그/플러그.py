import sys
input=sys.stdin.readline

n=int(input())
answer=-(n-1)
for _ in range(n):
    s=int(input())
    answer+=s

print(answer)