num = input()
count0 = 0
count1 = 0

if num[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(num)):
    if num[i] != num[i-1]:
        if num[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))