import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lighter = [[] for _ in range(N+1)]
heavier = [[] for _ in range(N+1)]
total = 0
std = N//2


def bfs(marble, which):
    global total
    queue = deque()
    visited = [False]*(N+1)
    visited[marble] = True
    queue.append(marble)
    cnt = 0
    while queue:
        num = queue.popleft()
        for n in which[num]:
            if not visited[n]:
                visited[n] = True
                cnt += 1
                if cnt > std:
                    total += 1
                    return
                queue.append(n)


for _ in range(M):
    i, j = map(int, input().split())
    lighter[i].append(j)
    heavier[j].append(i)


for marble in range(1, N+1):
    bfs(marble, lighter)
    bfs(marble, heavier)

print(total)


'''
###############################################################
# 태양오빠 코드

import sys
debug = False
if debug : sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split())
asc_edges = [[] for _ in range(n+1)]
des_edges = [[] for _ in range(n+1)]

for _ in range(m) :
    here, to = map(int, sys.stdin.readline().rstrip().split())
    asc_edges[here].append(to)
    des_edges[to].append(here)

asc_cnt = 0
des_cnt = 0
# 어떤 점을 기준으로 dfs 깊이를 찾는다
# 두번의 dfs로 만약 count가 내 뒤에 작은게 n//2 보다 많거나, 큰것이 n//2 보다 많으면 나는 중간이 못된다
# 모든 vertex에 대해 수행하고 카운트한 값을 리턴한다.
def asc_dfs(vtx, visit) :
    global asc_cnt
    if len(asc_edges[vtx]) == 0 :
        return
    for e in asc_edges[vtx] :
        if not visit[e] :
            visit[e] = True
            asc_dfs(e, visit)
            asc_cnt += 1


def des_dfs(vtx, visit) :
    global des_cnt
    if len(des_edges[vtx]) == 0 :
        return
    for e in des_edges[vtx] :
        if not visit[e] :
            visit[e] = True
            des_dfs(e, visit)
            des_cnt += 1

ret = 0
half = n // 2

for vertex in range(1,n + 1) :
    asc_visit = [False] * (n+1)
    des_visit = [False] * (n+1)
    asc_cnt = 0
    asc_dfs(vertex, asc_visit)
    des_cnt = 0
    des_dfs(vertex, des_visit)

    if debug : print(f'when node : {vertex}, asc : {asc_cnt}, des : {des_cnt}')
    if asc_cnt > half or des_cnt > half :
        ret += 1

print(ret)
'''