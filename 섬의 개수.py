import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(graph, w, h):
    cnt = 0
    visited = [[False] * w for _ in range(h)]
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
                    for d in range(8):
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

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    print(bfs(graph, w, h))
