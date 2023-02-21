from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N+1)]
visited = [False] * (N+1)

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

''' 
input
8

2 3 8
1 7
1 4 5
3 5
3 4
7
2 6 8
1 7 
'''