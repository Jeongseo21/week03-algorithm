import sys
import numpy as np
from collections import deque

input = sys.stdin.readline
T = int(input())
M, N, K = map(int, input().split())
dq = deque()
graph = [[0]*M for _ in range(N)]
result = 0

for _ in range(K):
    # i 가로, j 세로
    i, j = map(int, input().split())
    graph[j][i] = 1
graph = np.array(graph)


def bfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N or graph[y][x] == 0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        bfs(x-1, y)
        bfs(x+1, y)
        bfs(x, y-1)
        bfs(x, y+1)
        return True
    return False


for i in range(M):
    for j in range(N):
        if bfs(i,j) == True:
            result += 1
print(result)



