nodes = ('A', 'B', 'C', 'D', 'E', 'F')
distances = {
    'A': {'B': 2, 'C': 7, 'D': 6, 'F': 2},
    'B': {'A': 2, 'D': 1, 'F': 13},
    'C': {'A': 7, 'D': 5, 'E': 2},
    'D': {'A': 5, 'B': 1, 'C': 5, 'E': 5},
    'E': {'C': 2, 'D': 5, 'F': 10},
    'F': {'A': 2, 'B': 13, 'E': 10}}
 
unvisited = {node: float('inf') for node in nodes} 
visited = {}
current = 'A'
currentDistance = 0
unvisited[current] = currentDistance
 
while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is float('inf') or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
 
print(visited)