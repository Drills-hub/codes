import sys

n = int(sys.stdin.readline())
MOD = 1000000007

if n == 0:
    count = 1
elif n == 1:
    count = 1
else:
    dp = [0] * (n + 2)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 2):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    fibo_plus_1 = dp[n + 1]
    count = (2 * fibo_plus_1 - 1) % MOD

print(count)