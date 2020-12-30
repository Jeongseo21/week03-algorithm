import numpy as np
from collections import deque

h, w = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * w for _ in range(h)]


def check_air(graph):
    global visited
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if graph[ny][nx] == 1:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            queue.append((ny, nx))
            graph[ny][nx] = -1
    return graph

def melting_cheeze():


graph = check_air(graph)


graph = np.array(graph)
print(graph)
