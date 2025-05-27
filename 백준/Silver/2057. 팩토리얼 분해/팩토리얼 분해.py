import sys
input = sys.stdin.readline

n = int(input())

factor = [1, 1]  
for i in range(2, 21):  
    factor.append(factor[-1] * i)

factor = sorted(factor,reverse=True)


if n == 0:
    print("NO")
else:
    for num in factor:
        if n - num >= 0:
            n -= num
            if n == 0:
                print("YES")
                break
    else:
        print("NO")