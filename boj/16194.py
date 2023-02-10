n = int(input())
cp = [0] + list(map(int, input().split()))
dp = [0]

for i in range(1,n+1):
    dp.append(dp[i-1] + cp[1])
    for k in range(2, i+1):
        dp[i] = min(dp[i], dp[i-k] + cp[k])

print(dp[n])