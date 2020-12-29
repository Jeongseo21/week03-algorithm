# 연결 요소의 개수 - dfs로 푼 버전
N, M = map(int, input().split())

visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


def check(i):
    visited[i] = True
    for num in graph[i]:
        if not visited[num]:
            check(num)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        check(i)
        cnt += 1
print(cnt)
'''
# bfs로 푼 버전
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for y in adj_list[x]:
            if visited[y] == False:
                q.append(y)
                visited[y] = True
'''