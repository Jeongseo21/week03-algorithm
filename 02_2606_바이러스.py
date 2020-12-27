from collections import deque

count = 0
root_node = 1
N = int(input())
M = int(input())
visited = {}
graph = {i : [] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

queue = deque([root_node])

while queue:
    node = queue.popleft()
    if node not in visited.keys():
        visited[node] = True
        count += 1
        queue.extend(graph[node])
print(count-1)

