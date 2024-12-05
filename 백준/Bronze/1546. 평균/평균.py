def solution(N):

    answer = list(map(int, input().split()))
    avg = sum(answer) / max(answer) * 100 / N

    return avg


N = int(input())
print(solution(N))
