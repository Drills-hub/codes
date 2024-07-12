def solution(n):
    if 8000000000 > n > 0:
        answer = [int(i) for i in str(n)]
        answer.sort(reverse=1)
        answer_str=''.join(map(str,answer)) 
        return int(answer_str)
    else:
        return