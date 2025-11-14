import sys
input = sys.stdin.readline

def solution(n, k, a, b):
    day = 0
    catnip = [k] * n  
    
    while True:
        min_water = n * k + 1
        start_idx = 0
        
        for i in range(n - a + 1):
            current_sum = sum(catnip[i:i+a])
            if current_sum < min_water:
                min_water = current_sum
                start_idx = i
        
        for i in range(start_idx, start_idx + a):
            catnip[i] += b
        day += 1
        for i in range(n):
            catnip[i] -= 1
            if catnip[i] <= 0:
                return day

n, k, a, b = map(int, input().split())
print(solution(n, k, a, b))