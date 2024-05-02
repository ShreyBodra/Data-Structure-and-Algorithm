import heapq


def prim(graph):
    minimum_spanning_tree = []
    visited = set()
    start_vertex = list(graph.keys())[0]  # Start from any vertex

    # Initialize priority queue with edges from start_vertex
    priority_queue = [(0, start_vertex, None)]

    while priority_queue:
        weight, current_vertex, previous_vertex = heapq.heappop(priority_queue)
        if current_vertex not in visited:
            visited.add(current_vertex)
            if previous_vertex is not None:
                minimum_spanning_tree.append((previous_vertex, current_vertex, weight))
            for neighbor, edge_weight in graph[current_vertex].items():
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_vertex))

    return minimum_spanning_tree


# Example usage:
graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
