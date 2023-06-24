
import sys
import random
def dijkstra(graph, src):
    # Create a dictionary to store the minimum distance from the start node to each node
    dist = {node: sys.maxsize for node in graph}
    dist[src] = 0

    # Create a set to store visited nodes
    visited = set()

    while visited != set(graph):
        # Find the node closest to src
        minDist = sys.maxsize
        minNode = None
        for node in graph:
            if dist[node] < minDist and node not in visited:
                minDist = dist[node]
                minNode = node

        # Mark the current node as visited
        visited.add(minNode)

        # Update the distances of the neighboring nodes
        for neighbor, weight in graph[minNode].items():
            if dist[minNode] + weight < dist[neighbor]:
                dist[neighbor] = dist[minNode] + weight

    return dist

# Example usage:

def genRand(x, y):
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
src2 = '1'

graph2 = {
'1': {'2': 1,'8': 2},
'2': {'1': 1,'3': 1},
'3' :{'2': 1,'4':1},
'4': {'3': 1,'5':1},
'5': {'4':1,'6':1},
'6':{'5':1,	'7':1},
'7':{'6':1,	'8':1},
'8':{'7':1,	'1':2}
}
distances = dijkstra(graph, src)

# Print the minimum distances from the start node to all other nodes
for node, distance in distances.items():
    print(f"Minimum distance from {src} to {node}: {distance}")
