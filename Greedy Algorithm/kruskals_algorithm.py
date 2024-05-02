class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1, item2):
        self.parent[self.find(item1)] = self.find(item2)


def kruskals_algorithm(graph):
    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph['vertices'])
    edges = graph['edges']
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for edge in edges:
        source, destination, weight = edge
        if disjoint_set.find(source) != disjoint_set.find(destination):
            minimum_spanning_tree.append(edge)
            disjoint_set.union(source, destination)

    return minimum_spanning_tree

# Example usage:
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 10),
        ('A', 'C', 3),
        ('A', 'E', 8),
        ('B', 'D', 9),
        ('B', 'E', 5),
        ('C', 'E', 6),
        ('D', 'E', 14),
    ]
}

minimum_spanning_tree = kruskals_algorithm(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
