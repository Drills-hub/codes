num = int(input())

start = max(1, num - 9 * len(str(num)))

result = 0
for M in range(start, num):
    if M + sum(int(i) for i in str(M)) == num:
        result = M
        break

print(result)