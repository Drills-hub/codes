import sys
input = sys.stdin.readline

N = int(input())
marathoner = {}
for _ in range(N):
    name = input()
    marathoner[name] = marathoner.get(name, 0) + 1

for _ in range(N - 1):
    name = input()
    marathoner[name] = marathoner.get(name, 0) - 1

for name, cnt in marathoner.items():
    if cnt > 0:
        sys.stdout.write(name)
        break
