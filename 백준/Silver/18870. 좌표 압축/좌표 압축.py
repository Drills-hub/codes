import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
num_set = set(num_list)
num_idx = sorted(num_set)

num_dict = {num: idx for idx, num in enumerate(num_idx)}

for i in num_list:
    print(num_dict[i], end=' ')