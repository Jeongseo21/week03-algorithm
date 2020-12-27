from collections import deque

graph_list = {
    1: [2, 3],
    2: [1, 5],
    3: [1, 4],
    4: [3, 5],
    5: [2, 4]
}

root_node = 3

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            graph[node].sort(reverse=True)
            print(graph[node])
            stack.extend(graph[node])
    return visited
print(dfs(graph_list, 3))