R, C = map(int, input().split())
count = 0
graph = []
for _ in range(R):
    graph.append(input())

visited = []
answer = []
def dfs(x, y):
    global count
    node = graph[x][y]
    if  x < 0 or x >= R or y < 0 or y >= C or graph[x][y] in visited:
        return False
    if graph[x][y] not in visited:
        visited.append(graph[x][y])
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        count += 1
        answer.append(count)
        count = 0
print(dfs(0, 0))

