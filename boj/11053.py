n = int(input())
data = list(map(int, input().split()))
dp = [ 0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if(data[i] > data[j] and dp[i] < dp[j]):
            dp[i] = dp[j]
    dp[i] += 1
    #print(dp)
print(max(dp))
