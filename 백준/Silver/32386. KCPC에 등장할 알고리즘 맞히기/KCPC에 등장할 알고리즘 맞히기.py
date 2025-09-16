import sys

input = sys.stdin.readline

N = int(input())

count_dict = {}
max_count = 0
max_keys = []

for _ in range(N):
    tag_row = input().split()
    for tag in tag_row[2:]:
        count_dict[tag] = count_dict.get(tag, 0) + 1

max_count = max(count_dict.values())

for key, value in count_dict.items():
    if value == max_count:
        max_keys.append(key)

if len(max_keys) > 1:
    print(-1)
else:
    max_key = max_keys[0]
    print(max_key)