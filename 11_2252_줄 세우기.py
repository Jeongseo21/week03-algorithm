N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)

visited = [False]*(N+1)
stack = []


def dfs(i):
    global stack
    if not graph[i]:
        visited[i] = True
        stack.append(i)
        return
    for num in graph[i]:
        if visited[num]:
            continue
        else:
            dfs(num)
    visited[i] = True
    stack.append(i)


for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

stack = list(reversed(stack))
print(*stack)

