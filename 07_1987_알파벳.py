'''
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


##################################################################

'''

import sys
sys.setrecursionlimit(10000)
Y, X, V = 0, 1, 2

r, c = map(int, sys.stdin.readline().rstrip().split())
graph = [str(sys.stdin.readline().rstrip()) for _ in range(r)]
alpha_visit = [False] * 26 #[False for _ in range(26)]

dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]
ret = 1

def dfs0(x, y, cnt) : # pypy
    global ret
    # print_graph(alpha_visit)
    ret = max(ret, cnt)
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        if (0 <= xx < c) and (0 <= yy < r) :
            v = ord(graph[yy][xx])
            if not alpha_visit[v - 65] :
                alpha_visit[v - 65] = True
                dfs0(xx, yy, cnt+1)
                alpha_visit[v - 65] = False

alpha_visit[ord(graph[0][0]) - 65] = True
dfs0(0,0,ret)
print(ret)


