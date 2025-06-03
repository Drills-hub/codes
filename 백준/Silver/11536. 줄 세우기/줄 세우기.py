n = int(input())
name_list = [input().strip() for _ in range(n)]

increasing = True
for i in range(n-1):
    if name_list[i] > name_list[i+1]:
        increasing = False
        break

decreasing = True
for i in range(n-1):
    if name_list[i] < name_list[i+1]:
        decreasing = False
        break

if increasing:
    print("INCREASING")
elif decreasing:
    print("DECREASING")
else:
    print("NEITHER")