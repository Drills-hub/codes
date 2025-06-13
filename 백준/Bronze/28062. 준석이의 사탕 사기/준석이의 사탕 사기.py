n = int(input())
candy = list(map(int, input().split()))

total_candy = sum(candy)

if total_candy % 2 == 0:
    print(total_candy)
else:
    min_odd = float('inf')
    for i in candy:
        if i % 2 != 0:
            min_odd = min(min_odd, i)

    if min_odd != float('inf'):
        print(total_candy - min_odd)
    else:
        print(0) 