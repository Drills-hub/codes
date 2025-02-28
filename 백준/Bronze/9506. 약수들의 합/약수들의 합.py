def is_pretect(N):
    factor = []
    for i in range(1, N):
        if N % i == 0:
            factor.append(i)

    if sum(factor) == N:
        answer = []
        for i in range(len(factor)):
            if i == 0:
                answer.append(f"{factor[i]}")
            else:
                answer.append(f" + {factor[i]}")

        print(f"{N} =", "".join(answer))
    else:
        print(f"{N} is NOT perfect.")


while True:
    N = int(input())
    if N == -1:
        break
    else:
        is_pretect(N)