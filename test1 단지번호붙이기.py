
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input().strip()))
visited = [[0]*(N) for _ in range(N)]


def bfs(i, j, cnt):
    vcount = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    vcount += 1
    while queue:
        y, x = queue.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if graph[ny][nx] == '0':
                continue
            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            graph[ny][nx] = cnt
            queue.append((ny, nx))
            vcount += 1
    return vcount


answer = []
cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == 0:
            cnt += 1
            count = bfs(i, j, cnt)
            answer.append(count)

answer.sort()
print(cnt)
for i in range(cnt):
    print(answer[i])

