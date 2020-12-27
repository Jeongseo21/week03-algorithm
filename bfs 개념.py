from collections import deque

graph_list = {
    1: [2, 3],
    2: [1, 5],
    3: [1, 4],
    4: [3, 5],
    5: [2, 4]
}

root_node = 1

# bfs 넓이 우선 탐색

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print(bfs(graph_list, 3))
