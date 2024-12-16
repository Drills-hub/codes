s = list(map(int, input().split()))
n = [1, 1, 2, 2, 2, 8]

answer = []
for i in range(len(n)):
    answer.append(n[i] - s[i])

print(" ".join(map(str, answer)))
