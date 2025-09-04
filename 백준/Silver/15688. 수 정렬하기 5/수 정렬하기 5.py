import sys

input = sys.stdin.readline
print = sys.stdout.write

num_list = []
n = int(input())

for _ in range(n):
    num_list.append(int(input()))
num_list.sort()
print('\n'.join(map(str, num_list)))