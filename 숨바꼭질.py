import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([[N, 0]])
visited = [0]*(100010)
which = ['-1', '+1', '*2']

while queue:
    dis, cnt = queue.popleft()
    if dis == K:
        print(cnt)
        break
    for one in which:
        n_dis = eval(str(dis)+one)
        if n_dis < 0 or n_dis > 100000:
            continue
        if visited[n_dis] == 1:
            continue
        n_cnt = cnt + 1
        visited[n_dis] = 1
        queue.append([n_dis, n_cnt])


