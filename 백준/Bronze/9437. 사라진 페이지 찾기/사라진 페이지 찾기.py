while True:
    num = input().split()
    answer = []

    if num == ["0"]:
        break

    N = int(num[0])
    P = int(num[1])

    if P%2 == 0:
        i=P-1
        j=(N+1)-P
        k=(N+1)-i
    else:
        i=P+1
        j=(N+1)-P
        k=(N+1)-i

    answer.extend([i, j, k])
    answer.sort()
    answer = list(map(str, answer))
    print(" ".join(answer))