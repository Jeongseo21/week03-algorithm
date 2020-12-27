import sys
# import numpy as np
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, cnt):
    dq = deque()
    dq.append((y, x))
    visited[y][x] = 1
    graph[y][x] = cnt
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                dq.append((ny, nx))
                graph[ny][nx] = cnt
                visited[ny][nx] = 1

T = int(input())
answer = []
for _ in range(T):
    # 가로 M, 세로 N
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    result = 0

    for _ in range(K):
        # i 가로, j 세로
        i, j = map(int, input().split())
        graph[j][i] = 1
    # graph = np.array(graph)
    # print(graph)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                result += 1
                bfs(j, i, result)
    answer.append(result)

for _ in range(T):
    print(answer[_])












