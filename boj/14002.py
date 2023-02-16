n = int(input())
data = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if(data[i] > data[j]):  # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j]+1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰값을 대입

print(max(dp))  # 최장길이 출력

# 수열 출력
lcs = []
max_length = max(dp)

for i in range(n-1, -1, -1): # n-1 ~ 0
    if(dp[i] == max_length):
        lcs.append(data[i])
        max_length -= 1

print(*lcs[::-1])