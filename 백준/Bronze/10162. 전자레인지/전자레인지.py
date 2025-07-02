import sys
input = sys.stdin.readline

t = int(input())
buttons = [300, 60, 10]
answer = []

for btn in buttons:
    count, t = divmod(t, btn)
    answer.append(count)

if t == 0:
    print(" ".join(map(str, answer)))
else:
    print(-1)