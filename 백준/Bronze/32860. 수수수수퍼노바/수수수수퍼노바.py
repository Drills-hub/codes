import sys

input = sys.stdin.readline
N, M = map(int, input().split())

if M <= 26:
    view_name = chr(ord("A") + (M - 1))
else:
    k = M - 26
    first = (k - 1) // 26
    second = (k - 1) % 26
    view_name = chr(ord("a") + first) + chr(ord("a") + second)

print(f"SN {N}{view_name}")