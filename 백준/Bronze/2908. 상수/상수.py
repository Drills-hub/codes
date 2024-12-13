def solution(x, y):
    num_x = "".join(list(reversed(x)))
    num_y = "".join(list(reversed(y)))
    if int(num_x) > int(num_y):
        return num_x
    return num_y


x, y = input().split()
print(solution(x, y))
