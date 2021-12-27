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

def bfs_shortet_way(G, start, end):
    distances = [None] * N
    start_vertex = start
    distances[start_vertex] = 0
    parents = [None] * N
    queue = deque([start_vertex])
    while queue:
        cur_v = queue.popleft()
        for neighbor in G[cur_v]:
            if distances[neighbor] is None:
                parents[neighbor] = cur_v
                distances[neighbor] = distances[cur_v] + 1
                queue.append(neighbor)

    end_vertex = end
    path = [end_vertex]
    parent = parents[end_vertex]
    while parent not in None:
        path.append(parent)
        parent = parents[parent]

    return path
print(bfs_shortet_way(G,1,5))    