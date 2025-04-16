import itertools

A, B = input().split()
num_list = list(map(int, input().split()))
B = int(B)

max_sum = 0
for subset in itertools.combinations(num_list, 3):
    s = sum(subset)
    if s <= B and s > max_sum:
        max_sum = s

print(max_sum)