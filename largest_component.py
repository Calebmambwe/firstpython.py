def largest_component(graph):
    visited = set()

    largest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        largest = max(largest, size)

    return largest


def explore_size(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)

    return size