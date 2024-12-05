def solution():
    answer = set()

    for _ in range(10):
        N = int(input())
        i = N % 42
        answer.add(i)

    return len(answer)


print(solution())
