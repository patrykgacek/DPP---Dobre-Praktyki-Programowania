from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class BfsCommunityGraph:
    def __init__(self, graph: nx.Graph = None):
        self.graph: nx.Graph = graph
        self.levels: dict = {}
        self.spread_order: list = []
        self.start_node: str = None  # Changed to accept string nodes (names)

    def __str__(self) -> str:
        """
        Returns a string representation of the object, including graph details, levels, spread order, and the start node.
        """
        string_representation = (f"Graph Nodes: {self.graph.nodes()}\n"
                                 f"Graph Edges: {self.graph.edges()}\n"
                                 f"Levels: {self.levels}\n"
                                 f"Spread order: {self.spread_order}\n"
                                 f"Start node: {self.start_node}\n"
                                 f"Is Connected: {nx.is_connected(self.graph)}")
        return string_representation
  

    def draw(self):
        """
        Draws a visualization of the graph, with directed edges indicating the spread of information from the start node.
        """
        if not self.graph or not self.start_node:
            print("Graph or start node not set.")
            return
        
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(10, 8))
        nx.draw_networkx_nodes(self.graph, pos, node_size=700, node_color="lightblue")
        nx.draw_networkx_labels(self.graph, pos)
        
        directed_edges = [(self.spread_order[i], self.spread_order[i + 1])
                          for i in range(len(self.spread_order) - 1)]
        nx.draw_networkx_edges(self.graph, pos, edgelist=directed_edges, arrowstyle='->', arrowsize=20)
        
        plt.title("Spread of Information")
        plt.show()
  

    def set_start_node(self, node: str) -> bool:
        """
        Sets the start node for the BFS algorithm and initiates the BFS traversal.
        
        Parameters:
        node: The node to be set as the start node (should be a string representing a name).
        
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
        Checks if the given graph is valid for the BFS algorithm. Ensures all nodes are strings.
        
        Parameters:
        graph: nx.Graph: The graph to be validated.
        
        Returns: bool: True if the graph is valid, False otherwise.
        """
        # Ensure all nodes are strings
        return all(isinstance(node, str) for node in graph.nodes())

  
    def make_graph_from(self, edges: list) -> bool:
        """
        Creates a community graph from the given list of edges.
        
        Parameters:
        edges: list: A list of tuples representing edges between nodes.
        
        Returns: bool: True if the graph was created successfully, False otherwise.
        """
        if not edges:
            return False
        
        # Create a directed graph with string nodes
        G = nx.Graph()
        G.add_edges_from(edges)
        
        # Validate graph
        if not self.is_valid(G):
            return False

        self.graph = G
        return True


    def random_community(self, num_nodes: int, edge_prob: float, seed: int = None) -> bool:
        """
        Generates a random community graph with string nodes.
        
        Parameters:
        num_nodes: int: Number of nodes in the graph.
        edge_prob: float: Probability of an edge between nodes.
        seed: int (optional): Random seed for reproducibility.
        
        Returns: bool: True if the graph was generated successfully, False otherwise.
        """
        G = nx.erdos_renyi_graph(num_nodes, edge_prob, seed)
        
        # Assign unique names as node labels
        labels = {i: f"Person_{i}" for i in range(num_nodes)}
        G = nx.relabel_nodes(G, labels)
        
        self.graph = G
        return True
