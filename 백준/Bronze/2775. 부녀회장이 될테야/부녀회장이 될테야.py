t=int(input())
for _ in range(t):
    a=int(input())
    b=int(input())
    dp = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(1, b + 1):
        dp[0][i] = i

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    print(dp[a][b])