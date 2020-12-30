import sys
from collections import deque
input = sys.stdin.readline


def bfs(i):
    queue = deque()
    queue.append(i)
    while queue:
        now = queue.popleft()
        num = graph[now-1]
        if not visited[num]:
            visited[num] = True
            queue.append(num)


T = int(input())
for _ in range(T):
    N = int(input())
    graph = list(map(int, input().split()))
    visited = [False]*(N+1)
    cnt = 0

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(cnt)







