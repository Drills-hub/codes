import sys
input = sys.stdin.readline

N = int(input())
count = 0
for i in range(N):
    gitft = input().split("-")
    d_day = int(gitft[1])
    if d_day < 91:
        count += 1
print(count)