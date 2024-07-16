def solution(arr):
    arr.remove(min(set(arr)))
    answer=arr
    if not answer:
        return [-1]
    else:
        return answer