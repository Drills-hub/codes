def solution(T):
    answer = []
    for i in range(1, T + 1):
        x, y = map(int, (input().split()))
        answer.append(f"Case #{i}: {x} + {y} = {x+y}\n")

    return "".join(answer)


T = int(input())
print(solution(T))