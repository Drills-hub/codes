import sys
input = sys.stdin.readline

n = int(input())
min_quadrangle = float('inf')

if n == 1:
    min_quadrangle = 4
else:
    for a in range(int(n**0.5) + 2, 1, -1):
        b = (n + a - 1) // a
        if b < 2:
            b = 2
        perimeter = 2 * (a + b - 2)
        min_quadrangle = min(min_quadrangle, perimeter)

print(min_quadrangle)