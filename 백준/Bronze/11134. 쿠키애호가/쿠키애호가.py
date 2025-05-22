import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    answer=0
    a, b = map(int, input().split())
    answer+=a//b
    if a%b != 0:
        answer+=1
    print(answer)