# 빙산

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
melting = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def make_melting(graph, melting):

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                for d in range(4):
                    nx = j + dx[d]
                    ny = i + dy[d]
                    if nx < 0 or ny < 0 or nx >= M or ny >= N:
                        continue
                    if graph[ny][nx] == 0:
                        melting[i][j] += 1

    for i in range(N):
        for j in range(M):
            graph[i][j] = graph[i][j] - melting[i][j]
            melting[i][j] = 0
            if graph[i][j] < 0:
                graph[i][j] = 0

    return graph


def bfs(graph):
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
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
                        if nx < 0 or ny < 0 or nx >= M or ny >= N:
                            continue
                        if graph[ny][nx] == 0:
                            continue
                        if visited[ny][nx] == True:
                            continue
                        visited[ny][nx] = True
                        queue.append((ny, nx))
            cnt += 1
    return cnt




answer = 0
while True:
    ice_cnt = bfs(graph)
    if ice_cnt == 0:
        print(0)
        break
    elif ice_cnt >= 2:
        print(answer)
        break
    else:
        answer += 1
        graph = make_melting(graph, melting)


