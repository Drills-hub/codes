import sys
input = sys.stdin.readline

N = int(input())
left_counts = list(map(int, input().split()))

order = []
for height in range(N, 0, -1):
    order.insert(left_counts[height - 1], height)

print(" ".join(map(str, order)))