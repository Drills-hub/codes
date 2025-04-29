import sys
input = sys.stdin.readline

def absolute_value(N):
    a, b, c, d = N
    return [abs(a - b), abs(b - c), abs(c - d), abs(d - a)]

def same_num(N):
    return N[0] == N[1] == N[2] == N[3]


while True:
    a, b, c, d = map(int,input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    numbers = [a, b, c, d]
    count = 0

    while not same_num(numbers):
        numbers = absolute_value(numbers)
        count += 1

    print(count)
