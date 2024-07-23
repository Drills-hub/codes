def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        mat_plus = []
        for c, d in zip(a, b):
            mat_plus.append(c + d)
        answer.append(mat_plus)
    return answer