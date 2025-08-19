import sys

input = sys.stdin.readline
N, K = map(int, input().split())

exclude_digits = {K % 10, (2 * K) % 10}
answer = []
for i in range(1, N + 1):
    if i % 10 not in exclude_digits:
        answer.append(i)
        
print(len(answer))
print(" ".join(map(str, answer)))