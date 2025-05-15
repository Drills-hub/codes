n,k= map(int,input().split())


dp = [0] * n 
dp[0]=1

for i in range(1,n):
    for j in range(i,0,-1):
        dp[j]+=dp[j-1]

print(dp[k-1])
