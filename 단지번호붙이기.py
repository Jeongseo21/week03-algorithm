'''
from collections import deque

# 단지 번호 붙이기 - bfs 이해 못하고 만든 코드

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
answer = 0
def bfs(x, y):
    global answer
    dq = deque()
    dq.append((x, y))
    graph[y][x] = 0
    count = 1
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                count += 1
                graph[ny][nx] = 0
                print(graph)
                dq.append((nx, ny))
    if count != 0:
        result.append(count)
        answer += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)

result.sort()
print(answer)
for _ in range(answer):
    print(result[_])
'''
# 단지 번호 붙이기 - bfs 이해하고 만든 코드

import sys
from collections import deque
# import numpy as np
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[0]*N for _ in range(N)]

cnt = 0 # 단지 수

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = []

def bfs(y, x, cnt):
    count = 0
    dq = deque()
    dq.append((y, x))
    visited[y][x] = 1
    graph[y][x] = cnt
    count += 1

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx <0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[ny][nx] == 0 or visited[ny][nx] != 0:
                continue
            dq.append((ny, nx))
            count += 1
            visited[ny][nx] = 1
            graph[ny][nx] = cnt
    answer.append(count)


# main
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i,j,cnt) # 1단지부터 시작

print(cnt)
answer.sort()
for i in range(cnt):
    print(answer[i])
# graph = np.array(graph)
# print(graph)
