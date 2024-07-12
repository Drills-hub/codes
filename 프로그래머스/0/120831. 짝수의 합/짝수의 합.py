def solution(n):
    if 0 < n <= 1000:
        answer = sum(range(2, n + 1, 2))
        return answer
    else:
        return