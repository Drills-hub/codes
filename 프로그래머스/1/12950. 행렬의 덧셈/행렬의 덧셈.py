def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        Mat_plus = []
        for c, d in zip(a, b):
            Mat_plus.append(c + d)
        answer.append(Mat_plus)
    return answer