
num = list(map(int, input().split()))
num.sort(reverse=True)

a, b, c = num

for i in range(a,0,-1):
    a = i
    if a + b > c and a + c > b and b + c > a:
        print(a + b + c)
        break
    else:
        continue