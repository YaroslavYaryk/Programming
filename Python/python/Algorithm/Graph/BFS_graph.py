from collections import deque

M,N = map(int, input().split())
G = {}
for i in range(M):
    v1,v2 = map(int, input().split())
    for v,u in (v1,v2), (v2,v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)    

def bfs(G, start):
    distances = [None] * N
    start_vertex = start
    distances[start_vertex] = 0

    queue = deque([start_vertex])
    while queue:
        cur_v = queue.popleft()
        for neighbor in G[cur_v]:
            if distances[neighbor] is None:
                distances[neighbor] = distances[cur_v] + 1
                queue.append(neighbor)

    return distances

print(bfs(G,1))    