def solution(num):
    sum_num = (num + 1) * (num // 2)

    if num % 2 == 0:
        return print(sum_num)
    else:
        return print(sum_num + ((num // 2) + 1))


num = int(input())
solution(num)