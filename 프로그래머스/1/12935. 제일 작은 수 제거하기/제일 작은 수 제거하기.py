def solution(arr):
    arr.remove(min(set(arr)))
    if not arr:
        return [-1]
    else:
        return arr