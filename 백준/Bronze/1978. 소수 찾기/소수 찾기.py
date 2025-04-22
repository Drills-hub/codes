N = int(input())
num = list(map(int, input().split()))

count = 0

for i in range(N):
    if num[i] < 2:
        continue
    is_prime = True
    
    for j in range(2, int(num[i] ** 0.5) + 1):
        if num[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)