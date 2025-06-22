n = int(input())

milk=[]
answer=0
for _ in range(n):
    c = int(input())
    milk.append(c)
milk.sort(reverse=True)

# 3개씩 묶기
grouped_milk = []
for i in range(0, n, 3):
    grouped_milk.append(milk[i:i+3])

for group in grouped_milk:
    if len(group) != 3:
        answer += sum(group)
    else:
        group.sort()
        answer += group[1] + group[2]

print(answer)