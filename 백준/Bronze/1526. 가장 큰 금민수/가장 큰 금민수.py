n = int(input())

for i in range(n,1,-1):
    for j in str(i):
        if j not in ('4', '7'):
            break
    else:
        print(i)
        break