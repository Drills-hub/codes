import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 2000001  

for _ in range(N):
    n = int(input())
    count[n + 1000000] += 1  
result = []
for i in range(2000001):
    if count[i] > 0:
        result.extend([str(i - 1000000)] * count[i])

sys.stdout.write('\n'.join(result) + '\n')