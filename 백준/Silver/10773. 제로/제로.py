n=int(input())
answer = []
for i in range(n):
    num = int(input())

    if num == 0:
        answer.pop()
    else:
        answer.append(num)
print(sum(answer)) 