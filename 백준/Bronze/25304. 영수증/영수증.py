def solution(X, N):
    answer = 0
    for _ in range(N):
        x, y = map(int, input().split())
        answer += x * y

    if answer == X:
        return print("Yes")
    else:
        return print("No")


X = int(input())
N = int(input())

solution(X, N)