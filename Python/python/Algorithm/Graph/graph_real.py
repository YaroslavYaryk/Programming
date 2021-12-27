M,N = map(int, input().split())
G = {}
for i in range(M):
    v1,v2 = map(int, input().split())
    for v,u in (v1,v2), (v2,v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)    

print(G)

def dfs(vertex, G, used = None):
    used = used or set()
    used.add(vertex)
    for neighbor in G[vertex]:
        if  neighbor not in used:
            dfs(neighbor, G, used)
    return used

  

used = {}
N = 0
for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N+=1 
print(N)                   

