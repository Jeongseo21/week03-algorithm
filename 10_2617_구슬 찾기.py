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

