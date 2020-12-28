import sys
from string import ascii_uppercase
# sys.stdin = open("testcase/1987.txt", "r")

R, C = map(int, input().split())
count = 0
graph = []
for _ in range(R):
    graph.append(input())

visited = [[0]*C for _ in range(R)]
# alpha = list(ascii_uppercase)
check = set()

def dfs(x, y, cnt):
    global ans
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if x < 0 or x >= C:
            return
        elif y < 0 or y >= R:
            return
        elif graph[y][x] in check:
            return
        else:
            check.add(graph[y][x])
            dfs(nx, ny, cnt+1)
            check.remove(graph[y][x])

ans = 0
dfs(0, 0, ans)
print(ans)


