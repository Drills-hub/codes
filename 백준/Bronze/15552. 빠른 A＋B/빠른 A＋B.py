import sys

def solution(T):
    answer = []
    for _ in range(T):

        x, y = map(int, sys.stdin.readline().strip().split())
        answer.append(x + y)

    print("\n".join(map(str, answer)))

T = int(input().strip())
solution(T)
