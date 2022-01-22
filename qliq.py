import networkx as nx


g=nx.Graph()
edges=[(1,2),(2,3),(1,3),(3,4),(3,5)]
g.add_edges_from(edges)
res=nx.find_cliques(g)
i=0
for item in res:
    print(item)
    i+=1
print(i)
