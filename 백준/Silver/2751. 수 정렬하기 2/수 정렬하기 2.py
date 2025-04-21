import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 2000001  # -1,000,000 ~ 1,000,000

for _ in range(N):
    n = int(input())
    count[n + 1000000] += 1  # 인덱스 보정

for i in range(2000001):
    for _ in range(count[i]):
        print(i - 1000000)