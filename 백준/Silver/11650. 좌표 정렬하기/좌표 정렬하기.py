import sys
input=sys.stdin.readline
print=sys.stdout.write

N = int(input())
result = [tuple(map(int, input().split())) for _ in range(N)]
result.sort()
for x, y in result:
    print(f"{x} {y}"+"\n")