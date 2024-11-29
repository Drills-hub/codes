def solution(N):
    list_array = list(map(int, (input().split())))
    answer = [str(min(list_array)), str(max(list_array))]
    return " ".join(answer)


N = input()
print(solution(N))