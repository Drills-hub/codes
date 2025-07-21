import sys
input = sys.stdin.readline

n = int(input())
sticks=[]
counts = 1


for _ in range(n):
    sticks.append(int(input()))

max_height = sticks[-1]
for i in range(n-2, -1, -1):
    if sticks[i] > max_height:
        counts += 1
        max_height = sticks[i]

print(counts)