from collections import deque

N, M, V = map(int, input().split())
graph = { i : [] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)



visited_dfs = []
visited_bfs = []

def dfs(graph, root, visited):
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            graph[node].sort(reverse=True)
            stack.extend(graph[node])
    return visited

def bfs(graph, root, visited):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            graph[node].sort()
            queue.extend(graph[node])
    return visited

print(*dfs(graph, V, visited_dfs))
print(*bfs(graph, V, visited_bfs))