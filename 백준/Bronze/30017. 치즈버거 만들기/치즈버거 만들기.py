a, b = map(int, input().split())

a_case = 2 * b + 1
b_case = 2 * a - 1

print(min(a_case, b_case))