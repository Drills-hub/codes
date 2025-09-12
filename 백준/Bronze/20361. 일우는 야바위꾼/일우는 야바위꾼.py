import sys

input = sys.stdin.readline
N, X, K = map(int, input().split())

ball = X
for _ in range(K):
    a, b = map(int, input().split())
    if ball == a:
        ball = b
    elif ball == b:
        ball = a

print(ball)