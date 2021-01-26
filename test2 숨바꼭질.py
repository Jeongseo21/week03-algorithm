import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
which = ['-1', '+1', '*2']
visited = [0] * 100001

queue = deque()
queue.append([N, 0])

while queue:
    now, cnt = queue.popleft()
    if now == K:
        print(cnt)
        break
    for one in which:
        next = eval(str(now)+one)
        if next < 0 or next > 100000:
            continue
        if visited[next] == 0:
            visited[next] = 1
            queue.append([next, cnt+1])