import numpy as np
from collections import deque
# 가로 M, 세로 N
M, N = map(int, input().split())
dq = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
zero_cnt = 0
graph = []
visited = [[0]*M for _ in range(N)] # 방문처리용 이차원 배열

# graph와 visited 배열 생성
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(M):
        if temp[j] == 1:
            dq.append((i, j))
            visited[i][j] = 1
        elif temp[j] == -1:
            visited[i][j] = -1
        elif temp[j] == 0:
            zero_cnt += 1


def bfs():
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if graph[ny][nx] == -1:
                continue
            if visited[ny][nx] != 0:
                continue
            visited[ny][nx] = visited[y][x] + 1
            dq.append((ny, nx))


if zero_cnt == 0:
    print(0)
else:
    bfs()
    flag = False
    max_num = 0
    for i in range(N):
        if flag:
            break
        for j in range(M):
            if visited[i][j] == 0:
                print(-1)
                flag = True
                break
            elif visited[i][j] > max_num:
                max_num = visited[i][j]
    if visited[i][j] != 0 and max_num != 0:
        print(max_num - 1)
visited = np.array(visited)
print(visited)

'''
# 토마토 나은 풀이
from collections import deque

M, N = map(int, input().split())
box = []
q = deque()
for i in range(N):
    box.append(list(map(int, input().split())))

# 처음 익은 토마토 위치 큐에 삽입
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))

def bfs(M, N, box):
    day = -1
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while(q):
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if box[nx][ny] == 0:
                        box[nx][ny] = 1
                        q.append((nx, ny))
    for row in box:
        if 0 in row:
            return -1
    return day

answer = bfs(M, N, box)
print(answer)
'''









