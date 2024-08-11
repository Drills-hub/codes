def solution(a, b, n):
    answer = 0
    #n이 a보다 크거나 같을 때 반복
    while n >= a:
        if n % a == 0:
            n = (n//a)*b
            answer += n
        else:
            m = n % a
            n = (n//a)*b
            answer += n
            n = m + n
    return answer