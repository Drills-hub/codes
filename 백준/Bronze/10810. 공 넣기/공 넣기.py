def solution():
    N, M = map(int, input().split())
    answer = []
    for _ in range(N):
        answer.append("0")

    while M > 0:
        i, j, k = map(int, input().split())
        M = M - 1
        for x in range(i - 1, j):
            answer[x] = str(k)

    return " ".join(answer)


print(solution())
