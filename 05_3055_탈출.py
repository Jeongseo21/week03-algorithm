from collections import deque

R, C = map(int, input().split())
graph = []

for _ in range(R):
    graph.append(list(input()))

dochi = deque()
water = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            water.append((i, j))
        elif graph[i][j] == 'S':
            dochi.append((i, j))

day = 0
def bfs():
    global day
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while dochi:
        day += 1
        for _ in range(len(water)):
            y, x = water.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= C or ny >= R:
                    continue
                if graph[ny][nx] == '.':
                    graph[ny][nx] = day
                    water.append((ny, nx))

        for _ in range(len(dochi)):
            y, x = dochi.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= C or ny >= R:
                    continue
                if graph[ny][nx] == '.':
                    graph[ny][nx] = day
                    dochi.append((ny, nx))
                if graph[ny][nx] == 'D':
                    return day


answer = bfs()

if answer is None:
    print('KAKTUS')
else:
    print(answer)
