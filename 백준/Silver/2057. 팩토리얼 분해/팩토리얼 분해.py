import sys
input = sys.stdin.readline

n = int(input())
factor = [1]
for i in range(1, 21):
    next_fact = factor[-1] * i
    if next_fact > n:
        break
    factor.append(next_fact)

L = len(factor)
for mask in range(1, 1 << L):
    total = 0
    for i in range(L):
        if mask & (1 << i):
            total += factor[i]
            if total > n:
                break
    if total == n:
        print("YES")
        break
else:
    print("NO")