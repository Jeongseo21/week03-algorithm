


N = int(input())

graph = { i : [] for i in range(1, N+1)}

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

parent = [0]*(N+1)
stack = []


def dfs(i):
    global parent, stack
    stack.append(i)
    for j in graph[i]:
        if j not in stack:
            print('dfs 이전:', stack)
            dfs(j)
            print('                     dfs 이후:', stack)
            parent[stack[-1]] = stack[-2]
            stack.pop()

dfs(1)

print(stack)
print(parent)
# answer = parent[2:]
# for _ in range(N-1):
#     print(answer[_])
'''
# 제출 코드
import sys

sys.setrecursionlimit(100000)

N = int(input())

graph = {i: [] for i in range(1, N+1)}

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

parent = [0]*(N+1)
stack = []
visited = [False]*(N+1)

def dfs(i):
    global parent, stack
    stack.append(i)
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            parent[stack[-1]] = stack[-2]
            stack.pop()

dfs(1)

answer = parent[2:]
for i in range(N-1):
    print(answer[i])
'''