import sys
input = sys.stdin.readline

n = int(input())

straw = []
for _ in range(n):
    straw.append(int(input()))
straw.sort(reverse=True)

max_sum = -1
for i in range(n-2):
    if straw[i] < straw[i + 1] + straw[i + 2]:
        max_sum = max(max_sum, straw[i] + straw[i + 1] + straw[i + 2])
print(max_sum)