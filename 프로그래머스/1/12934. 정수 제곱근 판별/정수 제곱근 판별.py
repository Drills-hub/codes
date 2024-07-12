def solution(n):
    if n >= 1 :
        if int(n**0.5) == n**0.5 :
            sqrt_n = n**0.5
            return((sqrt_n+1)**2)
        else : return -1
    else:return
        

