N = int(input())
rgbd = [list(map(int, input().split())) for _ in range(N)]
ans = I = 1e9

for i in range(3):
    # 초기 값을 큰 값으로 설정하는 이유는 최솟값을 구해야 하니까..
    dp = [[I, I, I] for _ in range(N)]  
    dp[0][i] = rgbd[0][i]   # 처음 집을 R, G, B로 색칠
    for j in range(1,N):    # 두번째 집부터 색칠하면서 최소값 갱신
        dp[j][0] = rgbd[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgbd[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgbd[j][2] + min(dp[j-1][0], dp[j-1][1])
    for k in range(3):  # 첫번째 집과 N번째 집이 다른 경우만 골라내기
        if i != k:
            ans = min(ans, dp[-1][k])

print(ans)             

        
        
        