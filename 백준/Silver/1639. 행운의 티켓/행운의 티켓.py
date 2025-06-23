s = input()
n = len(s)

if n%2==0:
    start = n
else:
    start = n-1

answer = 0
for length in range(start, 1, -2):
    if answer!=0:

        break

    for i in range(n - length + 1):
        sub_s = s[i : i + length]
        half_length = length // 2

        left_sum = 0
        for k in range(half_length):
            left_sum += int(sub_s[k])

        right_sum = 0
        for k in range(half_length, length):
            right_sum += int(sub_s[k])

        if left_sum == right_sum:
            answer = length
            break

if not answer:  
    print(0)
else:
    print(answer)