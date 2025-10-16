def solution(s):
    s = list(map(int,s.split()))
    a,b= min(s),max(s)
    answer = f"{a} {b}"
    return answer