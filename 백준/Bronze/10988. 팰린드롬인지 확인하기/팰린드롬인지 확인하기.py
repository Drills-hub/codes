S = input()
def solution(S):
    if S == S[::-1]:
        return 1
    else:
        return 0

print(solution(S))