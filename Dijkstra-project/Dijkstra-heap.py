import sys
import heapq
import random

def dijkstra(graph, src):
    # Create a dictionary to store the minimum distance from the start node to each node
    dist = {node: sys.maxsize for node in graph}
    dist[src] = 0

    # Create a heap to store visited nodes
    heap = [(0, src)]

    while heap:
        # Find the node closest to src
        minDist, minNode = heapq.heappop(heap)
        if minDist > dist[minNode]:
            continue

        # Update the distances of the neighboring nodes
        for neighbor, weight in graph[minNode].items():
            newDist = dist[minNode] + weight

            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                heapq.heappush(heap, (newDist, neighbor))

    return dist

#Testing:

def genRand(x,y):
    return random.randint(x, y)


graph = {}
nodes = [chr(ord('A') + i) for i in range(26)]

for i in range(26):
    node = nodes[i]
    if i < 25:
        nextNode = nodes[i+1]
        graph[node] = {nextNode: genRand(1, 10)}
    else:
        graph[node] = {}


src = 'A'

distances = dijkstra(graph, src)

# Print the minimum distances from the start node to all other nodes
for node, distance in distances.items():
    print(f"Minimum distance from {src} to {node}: {distance}")
