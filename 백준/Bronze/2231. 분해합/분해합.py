num = int(input())

constructors = []
for M in range(num, 0, -1):
    sum_of_digits = sum(int(i) for i in str(M))
    constructor = M + sum_of_digits
    if constructor == num:
        constructors.append(M)

if not constructors:
    print(0)
else:
    print(min(constructors))