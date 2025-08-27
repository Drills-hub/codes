import sys

input = sys.stdin.readline

N, M = map(int, (input().split()))
A = list(map(int, input().split()))

# 누적합의 나머지 빈도수 활용
count = 0
prefix_mod = 0
rem = [0] * M
rem[0] = 1 
for x in A:
    prefix_mod = (prefix_mod + x) % M
    count += rem[prefix_mod]
    rem[prefix_mod] += 1

print(count)