import sys
input = sys.stdin.readline

def pado(n):
    dp = [0]*(n+3)
    if n < 4:
        return 1

    dp[1]=dp[2]=dp[3] = 1

    for i in range(4, n + 1):
        dp[i] = dp[i-2] + dp[i-3]
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(pado(n))