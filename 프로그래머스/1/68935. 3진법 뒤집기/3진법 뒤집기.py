def trit(x):
    trit_lst= []
    
    while x:
        trit_lst.append(str(x % 3))
        x //= 3
    return''.join(trit_lst[::-1])

def solution(n):
    answer = 0
    
    change = trit(n)
    
    for i in range(len(change)):
        answer += int(change[i]) * (3**i)
    
    return answer