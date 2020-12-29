import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
link = [[] for _ in range(N+1)]
parts = [0]*(N+1)
inDegree = [0]*(N+1)

for i in range(M):
    X, Y, Z = map(int, input().split())
    link[X].append([Y, Z])
    inDegree[Y] += 1

stack = [N]
parts[N] = 1

while stack:
    now = stack.pop()
    for i in range(len(link[now])):
        num, cnt = link[now][i]
        parts[num] += parts[now]*cnt
        inDegree[num] -= 1
        if inDegree[num] == 0:
            stack.append(num)

for i in range(1, N+1):
    if not link[i]:
        print(f'{i} {parts[i]}')




