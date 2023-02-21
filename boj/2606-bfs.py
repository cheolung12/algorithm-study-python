from collections import deque
N = int(input())
link = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(1)                
print(visited.count(True)-1)    