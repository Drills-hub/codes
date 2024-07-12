def solution(a, b):
    if a == b:
        return a or b
    else:
        n_min= min(a,b)
        n_max= max(a,b)
        answer= sum(range(n_min,n_max+1))
        return answer