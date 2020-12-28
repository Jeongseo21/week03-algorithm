import numpy as np
import sys
from collections import deque
#sys.stdin = open("testcase/7569.txt", "r")

# 가로 M, 세로 N, 높이 H
M, N, H = map(int, input().split())
graph = []
dq = deque()

zero_cnt = 0
# 3차원 그래프 만들기
for i in range(H):
    temp1 = []
    for j in range(N):
        temp2 = list(map(int, input().split()))
        for k in range(M):
            if temp2[k] == 1:
                dq.append((i, j, k))
            if temp2[k] == 0:
                zero_cnt += 1
        temp1.append(temp2)
    graph.append(temp1)

day = -1
# bfs
def bfs(day):

    dm = [-1, 1, 0, 0, 0, 0]
    dn = [0, 0, -1, 1, 0, 0]
    dh = [0, 0, 0, 0, -1, 1]
    while dq:
        day += 1
        for _ in range(len(dq)):
            h, n, m = dq.popleft()
            for i in range(6):
                nh = h + dh[i]
                nn = n + dn[i]
                nm = m + dm[i]
                if 0 > nh or nh >= H or 0 > nn or nn >= N or 0 > nm or nm >= M:
                    continue
                if graph[nh][nn][nm] == 0:
                    graph[nh][nn][nm] = graph[h][n][m] + 1
                    dq.append((nh, nn, nm))

    for h in range(H):
        for n in range(N):
            if 0 in graph[h][n]:
                return -1
    return day



answer = bfs(day)
print(answer)
#
# graph = np.array(graph)
# print(graph)