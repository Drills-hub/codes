import sys
input = sys.stdin.readline
n, x = map(int, input().split())
p_list = list(map(int, input().split()))

total_sum = sum(p_list)

if total_sum % x == 0:
    print(1)
else:
    print(0)