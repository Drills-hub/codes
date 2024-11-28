def solution():
    answer = []
    while True:
        A, B = map(int, (input().split()))
        if A != 0 or B != 0:
            answer.append(str(A + B))
        else:
            return print("\n".join(answer))


solution()