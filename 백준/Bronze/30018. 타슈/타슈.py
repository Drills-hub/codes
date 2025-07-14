n= int(input())
before = list(map(int, input().split()))
after = list(map(int, input().split()))

answer = 0
for i in range(n):
    if before[i] - after[i] < 0:
        answer += abs(before[i] - after[i])

print(answer)