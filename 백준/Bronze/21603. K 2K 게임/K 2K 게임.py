import sys

input = sys.stdin.readline
N, K = map(int, (input().split()))

K = K % 10
answer = []

for i in range(1, N + 1):
    if i % 10 != K and i % 10 != K * 2:
        answer.append(i)

print(len(answer))
print(" ".join(map(str, answer)))