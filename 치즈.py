import numpy as np
from collections import deque

h, w = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
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

def melting_cheeze(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        y, x = queue.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if visited[ny][nx]:
                continue
            if graph[ny][nx] == -1:
                graph[y][x] = 2
                continue

def bfs(graph):
    cnt = 0
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0 or visited[i][j]:
                continue
            else:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    y, x = queue.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if nx < 0 or ny < 0 or nx >= w or ny >= h:
                            continue
                        if graph[ny][nx] == 0:
                            continue
                        if visited[ny][nx] == True:
                            continue
                        visited[ny][nx] = True
                        queue.append((ny, nx))
            cnt += 1
    return cnt

graph = check_air(graph)

while bfs(graph) != 0:
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                melting_cheeze(i, j)

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 2:
                graph[i][j] = -1
    cnt += 1

graph = np.array(graph)
print(graph)
print(cnt)
