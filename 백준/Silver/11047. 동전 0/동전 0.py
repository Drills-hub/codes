import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
answer = 0
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if k >= i:
        answer += k // i
        k %= i
    else:
        pass
    
print(answer)