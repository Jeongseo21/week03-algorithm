import sys
import numpy as np
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    X, Y, Z = map(int, input().split())
    graph[X].append([Y, Z])


def dfs(i):
    stack = []
    len_node = 0
    while True:
        for node, length in graph[i]:
            len_node += length
            stack.append()


for i in range(1, N+1):
    if len(graph[i]) == 2:
        dfs(i)



