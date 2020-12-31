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
#  태양오빠풀이

import sys
sys.setrecursionlimit(10000)
Y, X, V = 0, 1, 2

r, c = map(int, sys.stdin.readline().rstrip().split())
graph = [str(sys.stdin.readline().rstrip()) for _ in range(r)]
alpha_visit = [False] * 26

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
dfs0(0, 0, ret)
print(ret)


##########################

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

c_list = [list(map(str, input().strip())) for _ in range(N)]
stack = []
alpha = list(range(65, 92, 1))

for x in range(N):
    for y in range(M):
        c_list[x][y] = ord(c_list[x][y])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

stack.append((0, 0))
c_list[0][0] = 100

while stack:

    x, y = stack.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if c_list[nx][ny] in alpha:
                alpha.remove(c_list[nx][ny])
                c_list[nx][ny] = c_list[x][y] + 1
                stack.append((nx, ny))

print(max(map(max, c_list)) - 99)

###################################################################

sys.setrecursionlimit(10000)
debug = False
Y, X, V = 0, 1, 2
if debug : sys.stdin = open('input.txt', 'r')
r, c = map(int, sys.stdin.readline().rstrip().split())
graph = [str(sys.stdin.readline().rstrip()) for _ in range(r)]
# if debug : print(ord('A')-65)
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
def print_graph(l : list) :
    print('-------------------------')
    print(l)

def dfs() : # TLE
    global ret
    stack = [[0, 0, alpha_visit[:], move_visit[:][:], 0]] # y, x, visit, cnt
    while stack :
        v = stack.pop()
        ret = max(ret, v[4])
        print_graph(move_visit)
        print(ret)
        if 0 <= v[Y] < r and 0 <= v[X] < c :
            if not v[V][ord(graph[ v[Y] ][ v[X] ]) - 65] and not v[3][ v[Y] ][ v[X] ] :
                v[V][ord(graph[ v[Y] ][ v[X] ]) - 65] = True
                v[3][ v[Y] ][ v[X] ] = True
                for i in range(4) :
                    stack.append([ v[Y] + dy[i], v[X] + dx[i], v[V][:], v[3][:][:], v[4] + 1 ])



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
# dfs()
alpha_visit[ord(graph[0][0]) - 65] = True
dfs0(0,0,ret)
# dfs2(0,0)
print(ret)












