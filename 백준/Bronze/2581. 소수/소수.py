M= int(input())
N = int(input())

prime = []

for i in range(M, N+1):
    if i < 2:
        continue
    is_prime = True
    
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))