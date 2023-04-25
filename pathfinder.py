from collections import deque

def getPath( edge_dictionary, node_dictionary, startNode, endNode, numNodes):
    graph = {}
    i = 0
    for i in range(0,numNodes):            
        graph[i] = {}
        for key in node_dictionary[i].nodesOut:
            graph[i][key] = edge_dictionary[str(i) + "," + str(key)].weight
    
    path = deque()
    distances, parentNode = dijkstra(graph,endNode)
    tempNode = startNode
    while tempNode != endNode:
        temp2 = parentNode[tempNode]
        path.appendleft(edge_dictionary[str(temp2) + "," + str(tempNode)])
        tempNode = temp2
    distances, parentNode = dijkstra(graph,startNode)

    
    tempNode = endNode
    while tempNode != startNode:
        temp2 = parentNode[tempNode]
        path.appendleft(edge_dictionary[str(temp2) + "," + str(tempNode)])
        tempNode = temp2
   

    return path




#code courtesy of chatgpt
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm implementation.

    Parameters:
    graph (dict): The graph represented as a dictionary of vertices and their respective neighbors and weights.
    start (int): The index of the starting vertex.

    Returns:
    A tuple containing two elements:
    - A dictionary of the shortest distances from the starting vertex to each vertex in the graph.
    - A dictionary of the previous vertices in the shortest path from the starting vertex to each vertex in the graph.
    """
    # Set the initial values for the distances and previous vertices.
    distances = {vertex: float('inf') for vertex in graph}
    previous_vertices = {vertex: None for vertex in graph}
    distances[start] = 0

    # Create a priority queue and add the starting vertex with distance 0.
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the vertex with the smallest distance from the priority queue.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Check if we have already found a shorter path to the current vertex.
        if current_distance > distances[current_vertex]:
            continue

        # Iterate over the neighbors of the current vertex and update their distances if necessary.
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices








