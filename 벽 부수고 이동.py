'''
import sys
from collections import deque

input = sys.stdin.readline
queue = deque([[0,0]])

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[0] * M for _ in range(N)]


def bfs():
    global magic
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            cnt += 1
            y, x = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or ny >= N or nx >= M:
                    continue

                if graph[ny][nx] == 1:
                    if visited[ny][nx] == 1:
                        continue
                    else:
                        visited[ny][nx] = 1
                elif graph[ny][nx] != 0:
                    continue
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])

bfs()

if graph[N-1][M-1] == 0 or graph[N-1][M-1] == 1:
    print(-1)
else:
    print(graph[N-1][M-1]+1)
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

dtroy = [[[0, 0] for _ in range(M)] for _ in range(N)]


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0, 0, 0)])
    dtroy[0][0][0] = 1  # 방문처리
    while queue:
        y, x, w = queue.popleft()
        if y == N-1 and x == M-1:
            return dtroy[y][x][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if dtroy[ny][nx][w]:
                continue
            if graph[ny][nx] == '0':
                dtroy[ny][nx][w] = dtroy[y][x][w] + 1
                queue.append((ny, nx, w))
            if graph[ny][nx] == '1' and w == 0:
                dtroy[ny][nx][1] = dtroy[y][x][w] + 1
                queue.append((ny, nx, 1))
    return -1

print(bfs())



















