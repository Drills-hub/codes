import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
i, j = 0, N - 1
count = 0
while i < j:
    s = a[i] + a[j]
    if s == x:
        count += 1
        i += 1
        j -= 1
    elif s < x:
        i += 1
    else:
        j -= 1

print(count)