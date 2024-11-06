def solution(common):
    
    interval_1 = common[2]-common[1]
    interval_2 = common[1]-common[0]
    
    if interval_1 - interval_2 ==0:
        answer = common[-1] + interval_1
        return answer
    
    else:
        interval_3 = interval_1/interval_2
        answer = common[-1] * interval_3
        return answer