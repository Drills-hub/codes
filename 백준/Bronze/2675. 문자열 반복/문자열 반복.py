def solution(S):
    answer = []
    for _ in range(S):
        x, y = input().split()
        for i in y:
            answer.append(i * int(x))
        answer.append("\n")

    return "".join(map(str, answer))


S = int(input())
print(solution(S))