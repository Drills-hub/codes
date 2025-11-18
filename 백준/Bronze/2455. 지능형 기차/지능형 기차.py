import sys
input = sys.stdin.readline

now=0
max_people=0
for _ in range(4):
    a,b=map(int,input().split())
    now+=b-a
    max_people=max(now, max_people)

print(max_people)