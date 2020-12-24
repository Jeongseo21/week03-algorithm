from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

graph.sort()
print(graph)

visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)