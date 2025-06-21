import sys

n = int(sys.stdin.readline())
count = 0

# a = 0인 경우
count += (2 * n + 1) ** 2

# a ≠ 0인 경우
for a in range(-n, n + 1):
    if a == 0:
        continue
    b_min = max(-n, 1 - a - n)
    b_max = min(n, 1 - a + n)
    if b_min <= b_max:
        count += (b_max - b_min + 1)
print(count)