def solution():
    N, M = map(int, input().split())
    answer = list(range(1, N + 1))

    for _ in range(M):
        i, j = map(int, input().split())
        answer[i - 1], answer[j - 1] = answer[j - 1], answer[i - 1]

    return " ".join(map(str, answer))


print(solution())