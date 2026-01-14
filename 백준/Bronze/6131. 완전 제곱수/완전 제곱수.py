count = 0
n=int(input())
for i in range(1,500):
    for j in range(1,500):
        if i*i - j*j==n:
            count +=1

print(count)