def solution(N, M):
    answer = list(range(1, N + 1))

    for _ in range(M):
        x, y = map(int, input().split())
        answer[x - 1 : y] = reversed(answer[x - 1 : y])

    return " ".join(map(str,answer))


N, M = map(int, input().split())
print(solution(N, M))
