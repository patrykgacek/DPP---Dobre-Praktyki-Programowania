from collections import deque
import networkx as nx

class BfsCommunityGraph:
  def __init__(self, graph: nx.Graph = None):
    self.graph: nx.Graph = graph
    self.levels: dict = {}
    self.spread_order: list = []
    self.start_node: int = None


  def __str__(self) -> str:
    """
    TODO: Should return a string representation of the object, e.g. the graph, levels, spread order, and the start node.
    """
    string_representation = f"Graph: {self.graph}\nLevels: {self.levels}\nSpread order: {self.spread_order}\nStart node: {self.start_node}, {nx.is_connected(self.graph)}\n"
    return string_representation
  

  def draw(self):
    """
    TODO: should draw a visualization of the resulting directed graph
    """
    pass
  

  def set_start_node(self, node: int) -> bool:
    """
    Sets the start node for the BFS algorithm, and runs it.
    TODO:node (int) shoud be changed to node (string) to be able to use string as a node name, e.g. firstname "Patryk, Kajetan, Artur", etc. or fullname e.g. "Patryk Gacek", etc.

    Parameters:
    node: The node to be set as the start node.

    Returns: bool: True if the node exists in the graph and is set as the start node, False otherwise.
    """
    if node in self.graph.nodes():
      self.start_node = node
      self.bfs()
      return True
    else:
      return False


  def bfs(self):
    """
    BFS (Breadth First Search) algorithm for the graph.
    """
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
    """
    Loads community graph from the given graph.

    Parameters:
    graph: nx.Graph: The graph to be loaded.

    Returns: bool: True if the graph is valid and loaded, False otherwise.
    """
    if self.is_valid(graph):
      self.graph = graph
      return True
    else:
      return False


  def is_valid(self, graph: nx.Graph) -> bool:
    """
    TODO: Checks if the given graph is valid for the BFS algorithm, also if the nodes are strings, e.g. firstnames, fullnames, etc.
    """
    return True

  
  def make_graph_from(self, edges: list) -> bool:
    """
    TODO: Creates a community graph from the given list of edges.
    """
    return True


  def radom_community(self, num_nodes: int, edge_prob: float, seed: int = None) -> bool:
    """
    Generates a random community graph.
    TODO: shoud generate graph with a string nodes, e.g. firstnames, fullnames, etc.
    """
    G = nx.erdos_renyi_graph(num_nodes, edge_prob, seed)
    self.graph = G
    return True