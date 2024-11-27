def solution(N):
    answer = []
    for _ in range(N // 4):
        answer.append("long")

    return " ".join(answer) + f" int"

N = int(input())
print(solution(N))