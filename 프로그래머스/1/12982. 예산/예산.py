def solution(d, budget):
    d_sort = sorted(d)
    answer = 0
    result = 0

    for i in d_sort:

        if answer + i <= budget:
            answer += i
            result += 1

    return result