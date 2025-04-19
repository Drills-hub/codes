N = int(input())
answer = []

for _ in range(N):
    n = int(input())
    answer.append(n)

answer.sort()
for i in answer:
    print(i)