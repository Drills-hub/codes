import sys
input = sys.stdin.readline

N, M, A, B = map(int, input().split())
chairs_needed = max(0, N * 3 - M)

if chairs_needed > 0:
    total_cost = chairs_needed * A + B
else:
    total_cost = 0
    
print(total_cost)