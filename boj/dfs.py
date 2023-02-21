N = int(input())
graph = [list(map(int, input().split())) for _ in range(N+1)]

visited = [False] * (N+1)

def dfs(graph, v, visited): # v는 시작값
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: 
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

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