n = int(input())
dp = []
for _ in range(n):
    dp.append([0]*3)

for i in range(n):
    RGB = list(map(int, input().split()))

    if i == 0:
        dp[0][0] = RGB[0]
        dp[0][1] = RGB[1]
        dp[0][2] = RGB[2]
    else:
        dp[i][0] = RGB[0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = RGB[1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = RGB[2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))