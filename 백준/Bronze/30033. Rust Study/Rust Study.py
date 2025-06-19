n = int(input())
plan = list(map(int, input().split()))
doing = list(map(int, input().split()))
answer = 0

for i in range(n):
    if doing[i] >= plan[i]:
        answer += 1

print(answer)