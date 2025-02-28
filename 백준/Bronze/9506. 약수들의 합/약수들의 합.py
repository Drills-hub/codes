def is_perfect(N):
    factors = [1]
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            factors.append(i)
            factors.append(N//i)

    if sum(factors) == N:
        answer = []
        for i in range(len(factors)):
            if i == 0:
                answer.append(f"{factors[i]}")
            else:
                answer.append(f" + {factors[i]}")

        print(f"{N} = {' + '.join(map(str, sorted(factors)))}")
    else:
        print(f"{N} is NOT perfect.")


while True:
    N = int(input())
    if N == -1:
        break
    is_perfect(N)