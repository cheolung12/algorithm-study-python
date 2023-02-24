from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 위치 확인
        for i in range(4):
            nx = x + dx[i]  # (1,1) -> (0,1) (2,1) (1,0) (1,2)
            ny = y + dy[i]

            # 미로 찾기 공간을 넘어간 경우 무시
            if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                continue
            # 이동할 수 없는 칸인 경우 무시
            if(maze[nx][ny] == 0):
                continue

            # 해당 노드를 처음 방문할 경우에만 최단 거리 기록
            if(maze[nx][ny] == 1):
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[N-1][M-1]

print(bfs(0,0))