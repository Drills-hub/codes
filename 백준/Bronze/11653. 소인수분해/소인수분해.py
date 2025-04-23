def prime_factorization(n):
    answer = []
    if n == 1:
        return []

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            answer.append(i)
            n //= i

    if n > 1:
        answer.append(n)
    return answer


N=int(input())
for num in prime_factorization(N):
    print(num)