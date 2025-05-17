import sys
input = sys.stdin.readline
n = int(input())

prev_num = 0
prev_num2 = 1
for i in range(2, n + 1):
    current = (prev_num + prev_num2)
    prev_num = prev_num2
    prev_num2 = current
print(prev_num2)