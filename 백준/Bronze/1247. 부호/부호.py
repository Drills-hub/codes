import sys
input = sys.stdin.readline

for _ in range(3):
    num_sum = 0
    N = int(input())
    for i in range(N):
        num_sum += int(input())
    if num_sum == 0:
        print(0)
    elif num_sum > 0:
        print("+")
    else:
        print("-")