import sys
input = sys.stdin.readline

N = int(input())
S = []
for i in range(1, N + 1):
    S.append(i)

answer = []
while len(S) != 1:
    answer.append(S.pop(0))
    S.append(S.pop(0))
answer.append(S.pop(0))
print(" ".join(map(str, answer)))