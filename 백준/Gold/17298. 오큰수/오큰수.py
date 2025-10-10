import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * N
stack = []

for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(" ".join(map(str, answer)))