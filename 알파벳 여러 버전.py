import sys
sys.setrecursionlimit(10000)
Y, X, V = 0, 1, 2

r, c = map(int, sys.stdin.readline().rstrip().split())
graph = [str(sys.stdin.readline().rstrip()) for _ in range(r)]
alpha_visit = [False] * 26

dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]
ret = 1


def bfs(sx, sy):
    queue = set()
    queue.add((sx, sy, graph[sx][sy]))
    global ret
    while queue:
        x, y, step = queue.pop()
        ret = max(ret, len(step))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in step:
                ns = step + graph[nx][ny]
                queue.add((nx, ny, ns))


alpha_visit[ord(graph[0][0]) - 65] = True
bfs(0, 0)
print(ret)