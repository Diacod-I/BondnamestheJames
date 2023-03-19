import networkx as nx
graph = nx.Graph()
graph.add_nodes_from([2,1,5,6])
graph.add_edge(7,8)
graph.add_edges_from([(1,3,{"friends":True,"weight":4}),(1,2),(1,5),(2,7),(2,8),(8,4),(3,6)])
print("\n",graph.edges.data("friends"),"\n")
print(graph.nodes,"\n")
print(graph.edges)
nx.draw(graph)