def solution():
    answer = []
    while True:
        try:
            A, B = map(int, (input().split()))
            answer.append(str(A + B))
        except EOFError:
            break

    return print("\n".join(answer))


solution()