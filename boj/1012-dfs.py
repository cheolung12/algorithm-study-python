import sys
sys.setrecursionlimit(10000)    # 재귀 깊이 설정

dx = [-1, 1, 0, 0]  # 방향벡터
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0  # 방문처리
        for i in range(4):  # 상하좌우 방문
            dfs(x + dx[i], y + dy[i])
        return True
    return False


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    cnt = 0     
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1
    print(cnt)