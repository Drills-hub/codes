import sys

input = sys.stdin.readline

N = int(input())

order = []
for _ in range(N):
    x = int(input())
    order.append(x)

order.sort()

min_number = 5  
right_pointer = 0
for i in range(N):
    while right_pointer < N and order[right_pointer] <= order[i] + 4:
        right_pointer += 1
    size = right_pointer - i  
    min_number = min(min_number, 5 - size)  

print(min_number)