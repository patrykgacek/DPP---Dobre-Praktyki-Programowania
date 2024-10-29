from collections import deque
import networkx as nx

class BfsCommunityGraph:
  def __init__(self, graph: nx.Graph = None):
    self.graph: nx.Graph = graph
    self.levels: dict = {}
    self.spread_order: list = []
    self.start_node: int = None

  def __str__(self) -> str:
    string_representation = f"Graph: {self.graph}\nLevels: {self.levels}\nSpread order: {self.spread_order}\nStart node: {self.start_node}, {nx.is_connected(self.graph)}\n"
    return string_representation
  
  def set_start_node(self, node: int) -> bool:
    # Zmiana wierzchołka startowego
    if node in self.graph.nodes():
      self.start_node = node
      self.bfs()
      return True
    else:
      return False

  def bfs(self):
    # Algorytm
    queue = deque([self.start_node])
    visited_nodes = set()
    self.levels[self.start_node] = 0
    self.spread_order.append(self.start_node)

    while queue:
      node = queue.popleft()
      visited_nodes.add(node)

      for neighbor in self.graph.neighbors(node):
        if neighbor not in visited_nodes:
          queue.append(neighbor)
          visited_nodes.add(neighbor)
          self.levels[neighbor] = self.levels[node] + 1
          self.spread_order.append(neighbor)
  

  def load_graph(self, graph: nx.Graph) -> bool:
    # Ładowanie własnego grafu społecznego
    if self.is_valid(graph):
      self.graph = graph
      return True
    else:
      return False


  def is_valid(self, graph: nx.Graph) -> bool:
    # TODO: czy spójny, nieskierowany itd. na potrzeby BFS w kontekście społeczności
    return True

  
  def make_graph_from(self, edges: list) -> bool:
    # TODO: zaimplementować z listy
    return True


  def radom_community(self, num_nodes: int, edge_prob: float, seed: int = None) -> bool:
    # Zainicjowanie losowego grafu społecznego
    G = nx.erdos_renyi_graph(num_nodes, edge_prob, seed)
    self.graph = G
    return True