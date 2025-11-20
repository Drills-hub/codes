y, m, d = map(int, input().split('-'))
n = int(input())

total = (y * 360) + ((m - 1) * 30) + (d - 1) + n
y = total // 360
total %= 360
m = total // 30
d = total % 30

print(f"{y}-{m+1:02d}-{d+1:02d}")