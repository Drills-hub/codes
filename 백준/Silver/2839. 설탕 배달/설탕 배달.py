import sys
input = sys.stdin.readline

N = int(input())
answer = -1

for x in range(N//3 + 1):
    rest = N - 3*x
    if rest % 5 == 0:
        y = rest // 5
        total = x + y
        if answer == -1 or total < answer:
            answer = total

print(answer)