N = input().strip()

result = 0
for num in N:
    num_int = int(num)
    if num_int > 4:
        num_int -= 1
    result = result * 9 + num_int
print(result)