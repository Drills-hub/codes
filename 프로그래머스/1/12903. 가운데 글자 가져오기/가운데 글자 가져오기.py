def solution(s):
    half = len(s)//2
    if len(s) % 2==0:
        answer = s[half-1:half+1]
        return answer
    else:
        answer = s[half]
        return answer


