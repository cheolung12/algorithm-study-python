N = int(input())
link = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(link):
    a, b = map(int, input().split()) 
    # 연결된 컴퓨터의 정보를 저장해준다.
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(v, cnt):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)
    return cnt        
    
print(dfs(1,0))
# print(graph)
#print(visited)