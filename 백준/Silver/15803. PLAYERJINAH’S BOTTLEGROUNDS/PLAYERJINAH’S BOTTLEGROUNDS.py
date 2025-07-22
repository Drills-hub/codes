import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

cross = (c - a) * (f - b) - (d - b) * (e - a)
if cross == 0:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")