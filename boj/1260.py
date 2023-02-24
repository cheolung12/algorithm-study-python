from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):  # 작은 수 부터 방문할 수 있게 정렬하자
    graph[i].sort()

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

dfs(graph, visited, V)
visited = [False] * (N+1)   # visited 초기화
print()
bfs(graph, visited, V)