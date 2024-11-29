def solution(N):
    list_array = list(map(int, (input().split())))
    min_num, max_num = float("inf"), float("-inf")

    for num in list_array:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return f"{min_num} {max_num}"


N = input()
print(solution(N))