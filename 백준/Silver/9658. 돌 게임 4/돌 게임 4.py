def stone_game(n):
    dp = [0] * (n + 5)
    
    dp[1] = 0
    dp[2] = 1
    dp[3] = 0
    dp[4] = 1
    
    for i in range(5, n + 1):
        if dp[i - 1] and dp[i - 3] and dp[i - 4]:
            dp[i] = 0
        else:
            dp[i] = 1
    
    return "SK" if dp[n] == 1 else "CY"

n = int(input())
print(stone_game(n))