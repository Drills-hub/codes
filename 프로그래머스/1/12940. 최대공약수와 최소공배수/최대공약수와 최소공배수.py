def gcd_solution(x,y): #최대 공약수 구하기
    if y == 0:
        return x
    else:
        return gcd_solution(y,x % y)

def solution(n, m):  #최소 공배수 구하기
    gcd = gcd_solution(n,m)
    lcm = (n*m)//gcd
    answer = [gcd,lcm]
    
    return answer

