import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
link = [[] for _ in range(N+1)]
count = [0]*(N+1)
inDegree = [0]*(N+1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    link[X].append((Y, Z))
    inDegree[Y] += 1

count[N] = 1

stack = [N]
while stack:
    now = stack.pop()
    for part, cnt in link[now]:
        count[part] += cnt * count[now]
        inDegree[part] -= 1
        if inDegree[part] == 0:
            stack.append(part)

for i in range(1, N+1):
    if not link[i]:
        print(f'{i} {count[i]}')