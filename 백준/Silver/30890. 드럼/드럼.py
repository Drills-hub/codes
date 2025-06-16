x,y = map(int, input().split())

left = []
right = []

for i in range(1, x + 1):
    a= i / x
    if a <=1:
        left.append(a)

for j in range(1, y + 1):
    b= j / y
    if  b <= 1:
        right.append(b)

beat = sorted(set(left + right))

result = []
for i in beat:
    if i in left and i in right:
        result.append(3)
    elif i in left:
        result.append(1)
    else:
        result.append(2)

print("".join(map(str, result)))