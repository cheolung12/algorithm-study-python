n = int(input())
cp = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], cp[k] + dp[i-k])

print(dp[n])