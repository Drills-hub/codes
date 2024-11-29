def solution(N, X):
    answer = []
    list_array = list(map(int, (input().split())))

    for i in range(len(list_array)):
        if list_array[i] < X:
            answer.append(str(list_array[i]))
    return " ".join(answer)


N, X = map(int, (input().split()))
print(solution(N, X))