import sys, heapq
input = sys.stdin.readline

n = int(input())
large_n = []

for _ in range(n):
    for x in map(int, input().split()):
        if len(large_n) < n:
            heapq.heappush(large_n, x)
        elif large_n[0] < x:
            heapq.heapreplace(large_n, x)


print(large_n[0])