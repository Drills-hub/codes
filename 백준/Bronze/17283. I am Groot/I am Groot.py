import sys

input = sys.stdin.readline

L = int(input())
R = int(input())

total_branch_length = 0
current_length = L
num_branches = 2

while True:
    next_length = int(current_length * R / 100)
    if next_length <= 5:
        break

    total_branch_length += num_branches * next_length

    current_length = next_length
    num_branches *= 2

print(total_branch_length)