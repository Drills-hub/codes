import sys
input = sys.stdin.readline

A, B = map(int, input().split())
K, X = map(int, input().split())

count = 0
max_friend = K + X
min_friend = K - X

if min_friend > B or max_friend < A:
    print("IMPOSSIBLE")
else:
    start = max(min_friend, A)
    end = min(max_friend, B)
    count = end - start + 1
    print(count)