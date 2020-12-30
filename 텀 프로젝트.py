import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def bfs(i):
    queue = deque()
    queue.append((i, 1))
    start = i
    visited[i] = True
    while queue:
        now = queue.popleft()
        num = graph[now[0]-1]
        if visited[num] and num == start :
            return True
        if not visited[num]:
            visited[num] = True
            queue.append((num, now[1]+1))
    return False


for _ in range(T):
    n = int(input().strip())
    graph = list(map(int, input().split()))
    visited = [False]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if not bfs(i):
               cnt += 1
    print(cnt)



