L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

lower_bound = 0
for x in S:
    if x < n:
        lower_bound = x
    else:
        upper_bound = x 
        break 


if n in S:
    print(0)
else:

    count = (n - lower_bound) * (upper_bound - n) - 1
    print(count)