from models.bfs_community_graph import BfsCommunityGraph
import networkx as nx

# 1. Stworzenie obiektu klasy BfsCommunityGraph
community_graph = BfsCommunityGraph()

# 2. Stworzenie grafu z listy krawędzi
edges = [("Patryk", "Kajetan"), ("Kajetan", "Artur"), ("Patryk", "Julia"), 
         ("Julia", "Anna"), ("Anna", "Zosia"), ("Zosia", "Kajetan")]
community_graph.make_graph_from(edges)

# 3. Ustawienie węzła startowego (np. "Patryk") i uruchomienie algorytmu BFS
start_node = "Patryk"
if community_graph.set_start_node(start_node):
    print(f"Algorytm BFS rozpoczęty od węzła: {start_node}")
else:
    print("Podany węzeł startowy nie istnieje w grafie.")

# 4. Wyświetlenie wyników BFS
print("Wynik BFS (rozprzestrzenianie się informacji):")
print("Kolejność rozprzestrzeniania:", community_graph.spread_order)
print("Poziomy (dystans) do startowego węzła:", community_graph.levels)

# 5. Narysowanie grafu rozprzestrzeniania się informacji
community_graph.draw()

graph = BfsCommunityGraph()
graph.random_community(10, 0.2)
graph.set_start_node(0)

print(graph)
