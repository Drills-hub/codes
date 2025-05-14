import math, sys
input = sys.stdin.readline

k = input().strip()

if '.' not in k:
    print("NO")
    exit()

float_k = float(k)


decimal_part = k.split('.')[1]

p = int(decimal_part)
q = 10 ** len(decimal_part)

gcd_pq = math.gcd(p, q)

simplified_p = p // gcd_pq
simplified_q = q // gcd_pq


approx = simplified_p / simplified_q

if abs(float_k - approx) <= 10 ** -6:
    print("YES")
    print(simplified_p, simplified_q)
else:
    print("NO")
