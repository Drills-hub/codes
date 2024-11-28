def solution(T):
    answer = []
    for i in range(1, T + 1):
        answer.append(" " * (T - i) + "*" * i + "\n")

    return "".join(answer)


T = int(input())
print(solution(T))