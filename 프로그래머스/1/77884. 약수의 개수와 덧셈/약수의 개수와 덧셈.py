
def measure(n):
    measure = 0
    for i in range(1, n+1):
        if n % i == 0:
            measure += 1
    return measure


def solution(a, b):
    result = 0
    for n in range(a, b+1):
        if measure(n) % 2 == 0:
            result += n
        else:
            result -= n
    return result


print(solution(13, 17))
