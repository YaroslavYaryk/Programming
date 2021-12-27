from collections import deque

m, n  = map(int, input().split())
for i in range(m):
    v1, v2 = map(int, input().split())
    graph = {i: set()  for i in range(n)}
    graph[v1].add(v2)
    graph[v2].add(v1)


distance = [None] * n
start = 0
distance[start] = 0
queue = deque([start])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            queue.append(neigh_v)
    print(distance)       






















graph = [ [1,4,5], [0,2,6], [1,3,7], [2,4,8], [0,3,9], [0,7,8], [1,8,9], [2,5,9], [3,5,6], [4,6,7] ] 

# def bfs(graph, vertices):
#     visited = {vertices}
#     to_explore = [vertices]
#     verth = dict()
#     verth[vertices] = 0
#     prev = dict()
#     prev[vertices] = vertices
#     while to_explore:
#         u = to_explore.pop(0)
#         # print (u)
#         new_vertices = [i for i in graph[u] if i not in visited]
#         for i in new_vertices:
#             verth[i] = verth[vertices] +1
#             prev[i] = u
#         to_explore.extend(new_vertices)
#         visited.update(new_vertices)

#     for i in verth:
#         print(i, verth[i])
    
#     print("------------------------")
    
#     for i in prev:
#         print(i, prev[i])


# (bfs(graph,0))        






