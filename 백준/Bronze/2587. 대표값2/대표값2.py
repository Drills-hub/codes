answer = []

for _ in range(5):
    n = int(input())
    answer.append(n)

answer.sort()

print(sum(answer) // 5)
print(answer[2])