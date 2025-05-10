while True:
    Num = input().split()
    answer = []

    if Num == ["0"]:
        break

    N = int(Num[0])
    P = int(Num[1])

    if P%2 == 0:
        i=P-1
        answer.append(i)
        j=(N+1)-P
        answer.append(j)
        k=(N+1)-i
        answer.append(k)
    else:
        i=P+1
        answer.append(i)
        j=(N+1)-P
        answer.append(j)
        k=(N+1)-i
        answer.append(k)

    answer.sort()
    answer = list(map(str, answer))
    print(" ".join(answer))