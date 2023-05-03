from collections import deque

def getPath( edge_dictionary, node_dictionary, startNode, endNode):
    graph = {}
    i = 0
    numNodes = len(node_dictionary)
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


import heapq

def astar(graph, start, goal, heuristic):
    """
    A* algorithm implementation.

    Parameters:
    graph (dict): The graph represented as a dictionary of vertices and their respective neighbors and weights.
    start (int): The index of the starting vertex.
    goal (int): The index of the goal vertex.
    heuristic (function): The heuristic function that estimates the distance between a vertex and the goal vertex.

    Returns:
    A tuple containing two elements:
    - A list of the vertices in the shortest path from the starting vertex to the goal vertex.
    - The length of the shortest path from the starting vertex to the goal vertex.
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

        # Check if we have already found the goal vertex.
        if current_vertex == goal:
            break

        # Iterate over the neighbors of the current vertex and update their distances if necessary.
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                priority = distance + heuristic(neighbor, goal) # Calculate priority using the heuristic function
                heapq.heappush(priority_queue, (priority, neighbor))

    # Reconstruct the shortest path from the start to the goal.
    path = []
    current_vertex = goal
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.reverse()

    return path, distances[goal]









