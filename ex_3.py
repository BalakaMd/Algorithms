import heapq


def dijkstra(graph, start):
    """
    Implementation of Dijkstra's algorithm to find the shortest path in a graph.
    Parameters:
    - graph: a dictionary representing the weighted graph where keys are vertices and values are dictionaries
     of neighbors and weights
    - start: the starting vertex for the algorithm
    Returns:
    - distances: a dictionary containing the shortest distances from the start vertex to all other vertices
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    unvisited = [(0, start)]

    while unvisited:
        current_distance, current_vertex = heapq.heappop(unvisited)

        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))

    return distances


# Приклад використання:
test_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
print(dijkstra(test_graph, start_vertex))
