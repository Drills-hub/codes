n = sorted(list(map(int, input().split())))
m = int(input())

answer = []
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] + n[j] == m:
            if (n[i], n[j]) not in answer:
                answer.append((n[i], n[j]))

answer.sort()
for i in answer:
    print(*i)
print(len(answer))