def solution(N):

    answer = []
    list_array = input().split()
    v = input()

    for i in range(len(list_array)):
        if list_array[i] == v:
            answer.append(list_array[i])
    return print(len(answer))


N = int(input())
solution(N)