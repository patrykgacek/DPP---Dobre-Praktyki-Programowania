from models.bfs_community_graph import BfsCommunityGraph

graph = BfsCommunityGraph()
graph.radom_community(10, 0.2)
graph.set_start_node(0)

print(graph)
