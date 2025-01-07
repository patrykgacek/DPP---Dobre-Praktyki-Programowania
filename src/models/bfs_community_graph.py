import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from networkx import Graph, DiGraph
from typing import List, Tuple, Dict

SPREAD_TITLE = "Spread of Information"
CONNECTIONS_TITLE = "Social Network Connections"


class BfsCommunityGraph:
    """
    Impletentation of the BFS algorithm for analyzing information spread in social networks.

    :param graph: Graph object representing the social network
    :param start_node: The node to start the BFS traversal from
    :param debug: Flag for printing debug information during the BFS algorithm
    """

    def __init__(self, graph: Graph = None, start_node: str = None, debug: bool = False):
        self.graph: Graph = graph  # Social network graph
        self.start_node: str = start_node  # Start node for BFS algorithm
        self.spread_graph: DiGraph = None  # Spread information graph
        self.bfs_deep: int = 0  # deepest level of the result graph
        self.bfs_order: List[str] = []  # Order of visited nodes
        self.bfs_debug: bool = debug  # Debug flag for BFS algorithm

    def __str__(self) -> str:
        """
        Return the string representation of the graph.

        :return: String representation of the graph
        """
        gstr = (
            f"Graph Nodes: {self.graph.nodes() if self.graph else '-'}\n"
            f"Graph Edges: {self.graph.edges() if self.graph else '-'}\n"
            f"Deep: {self.bfs_deep}\n"
            f"Spread order: {self.bfs_order}\n"
            f"Start node: {self.start_node}\n"
            f"Is Connected: {nx.is_connected(self.graph) if self.graph else '-'}\n"
            f"Result graph nodes: {self.spread_graph.nodes() if self.spread_graph else '-'}\n"
            f"Result graph edges: {self.spread_graph.edges() if self.spread_graph else '-'}\n"
        )
        return gstr

    def is_valid(self) -> bool:
        """
        Check if the graph is valid for BFS algorithm.

        :return: True if the graph is valid, False otherwise
        """
        valid = True
        if not self.graph:
            print("Error: Graph is not set.")
            valid = False

        if valid and not isinstance(self.start_node, str):
            print("Error: Start node should be a string.")
            valid = False

        if valid and not all(isinstance(node, str) for node in self.graph.nodes):
            print("Error: Nodes should be strings.")
            valid = False

        if valid and self.start_node not in self.graph.nodes:
            print("Error: Start node is not in the graph.")
            valid = False

        if not valid:
            print(
                "Please resolve the above issues before analyzing information spread in social networks."
            )

        return valid

    def __print_log(self, message: str) -> None:
        """
        Print log message if debug flag is set.

        :param message: Log message to print
        """
        if self.bfs_debug:
            print(message)

    def __bfs(self) -> List[str]:
        """
        Perform BFS traversal starting from the given node.

        :return: List of nodes in BFS order
        """
        self.spread_graph = nx.DiGraph()
        visited = set()
        queue = deque([(self.start_node, 0)])
        bfs_order = []

        visited.add(self.start_node)
        self.spread_graph.add_node(self.start_node)

        while queue:
            self.__print_log(f"Queue: {queue}")
            node, level = queue.popleft()
            self.__print_log(f"Visiting {node} at level {level}")
            bfs_order.append({node: level})

            self.__print_log(f"Neighbors of {node}: {list(self.graph.neighbors(node))}")
            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    self.__print_log(f"Adding {neighbor} to the queue")
                    next_level = level + 1
                    queue.append((neighbor, next_level))
                    self.bfs_deep = max(self.bfs_deep, next_level)
                    visited.add(neighbor)
                    self.spread_graph.add_node(neighbor)
                    self.spread_graph.add_edge(node, neighbor)
                else:
                    self.__print_log(f"Skipping {neighbor}")

        self.__print_log(f"BFS end. Order: {bfs_order}")
        self.bfs_order = bfs_order
        return bfs_order

    def __clean_results(self) -> None:
        """
        Clean the results of the BFS algorithm.
        """
        self.bfs_order = []
        self.start_node = None
        self.spread_graph = None

    def __calc_node_colors(self, cmap: plt.cm) -> plt.cm:
        """
        Return a colormap for coloring nodes based on their levels.

        :param cmap: Colormap object

        :return: Calculated colormap for coloring nodes
        """
        levels = [list(node.values())[0] for node in self.bfs_order]
        norm = plt.Normalize(levels[0], levels[-1])
        return cmap(norm(levels))

    def run(self, start_node: str = None) -> List[Dict[str, int]]:
        """
        Run the BFS algorithm and return the results.

        :param start_node: The node to start the BFS traversal from

        :return: List of nodes in BFS order
        """
        if start_node:
            self.start_node = start_node
        else:
            self.start_node = list(self.graph.nodes)[0] if self.graph else None

        if not self.is_valid():
            return {}

        self.__bfs()
        return self.bfs_order

    def make_graph(self, nodes: List[str], edges: List[Tuple[str, str]]) -> None:
        """
        Create a graph from the given nodes and edges.

        :param nodes: List of nodes in the graph
        :param edges: List of edges in the graph
        """
        self.__clean_results()
        self.graph = nx.Graph()
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(edges)

    def random_community(self, num_nodes: int, edge_prob: float, seed: int = None) -> None:
        """
        Generate a random community graph with string nodes.

        :param num_nodes: Number of nodes in the graph
        :param edge_prob: Probability of an edge between nodes
        :param seed: Random seed for reproducibility
        """
        self.__clean_results()
        self.graph = nx.erdos_renyi_graph(num_nodes, edge_prob, seed)
        labels = {i: f"Person_{i}" for i in range(num_nodes)}
        self.graph = nx.relabel_nodes(self.graph, labels)

    def draw_connections(
        self,
        figsize: Tuple[int, int] = (10, 8),
        node_size: int = 2000,
        node_color: str = "lightblue",
        edge_color: str = "gray",
    ) -> None:
        """
        Draw the connections of the graph.

        :param figsize: Figure size for the plot
        :param node_size: Size of the nodes
        :param node_color: Color of the nodes
        :param edge_color: Color of the edges
        """
        if not self.graph:
            print("Error: Graph is not set. Load some data first.")
            return

        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=figsize)
        nx.draw_networkx_nodes(self.graph, pos, node_size=node_size, node_color=node_color)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos, edge_color=edge_color, arrows=False)
        plt.title(CONNECTIONS_TITLE)
        plt.show()

    def draw_spread(
        self,
        figsize: Tuple[int, int] = (10, 8),
        node_size: int = 2000,
        edge_color: str = "gray",
        cmap: plt.cm = plt.cm.summer,
        alpha: float = 0.5,
        arrow_style: str = "-|>",
        arrow_size: int = 20,
    ) -> None:
        """
        Draw the spread of information from the start node.

        :param figsize: Figure size for the plot
        :param node_size: Size of the nodes
        :param edge_color: Color of the edges
        :param cmap: Colormap for coloring nodes based on their levels
        :param alpha: Transparency of the nodes
        """
        if not self.spread_graph:
            print("Error: Spread graph is not set. Use BfsCommunityGraph.run() method first.")
            return

        plt.figure(figsize=figsize)
        pos = nx.spring_layout(self.spread_graph)
        node_colors = self.__calc_node_colors(cmap)
        nx.draw_networkx_nodes(
            self.spread_graph,
            pos,
            node_size=node_size,
            alpha=alpha,
            node_color=node_colors,
        )
        nx.draw_networkx_labels(
            self.spread_graph,
            pos,
        )
        nx.draw_networkx_edges(
            self.spread_graph,
            pos,
            edge_color=edge_color,
            arrows=True,
            arrowstyle=arrow_style,
            node_size=node_size,
            arrowsize=arrow_size,
        )
        plt.title(f"{SPREAD_TITLE} from {self.start_node}")
        plt.show()

    def draw_compare(
        self,
        figsize: Tuple[int, int] = (20, 8),
        node_size: int = 2000,
        node_color: str = "lightblue",
        edge_color: str = "gray",
        spread_cmap: plt.cm = plt.cm.summer,
        spread_arrow_size: int = 20,
        spread_alpha: float = 0.5,
        spread_arrow_style: str = "-|>",
    ) -> None:
        """
        Draw the original graph and the spread graph side by side.

        :param figsize: Figure size for the plot
        :param node_size: Size of the nodes
        :param node_color: Color of the nodes
        :param edge_color: Color of the edges
        :param spread_cmap: Colormap for coloring nodes based on their levels
        :param spread_arrow_size: Size of the arrows
        :param spread_alpha: Transparency of the nodes
        :param spread_arrow_style: Style of the arrows
        """
        if not self.graph or not self.spread_graph:
            print("Error: Compares is not available. Load some data and run BFS first.")
            return

        _, axes = plt.subplots(1, 2, figsize=figsize)

        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_nodes(
            self.graph, pos, ax=axes[0], node_size=node_size, node_color=node_color
        )
        nx.draw_networkx_labels(self.graph, pos, ax=axes[0])
        nx.draw_networkx_edges(self.graph, pos, ax=axes[0], edge_color=edge_color, arrows=False)
        axes[0].set_title(CONNECTIONS_TITLE)

        pos = nx.spring_layout(self.spread_graph)
        node_colors = self.__calc_node_colors(spread_cmap)
        nx.draw_networkx_nodes(
            self.spread_graph,
            pos,
            ax=axes[1],
            node_size=node_size,
            alpha=spread_alpha,
            node_color=node_colors,
        )
        nx.draw_networkx_labels(self.spread_graph, pos, ax=axes[1])
        nx.draw_networkx_edges(
            self.spread_graph,
            pos,
            ax=axes[1],
            edge_color=edge_color,
            arrows=True,
            arrowstyle=spread_arrow_style,
            node_size=node_size,
            arrowsize=spread_arrow_size,
        )
        axes[1].set_title(f"{SPREAD_TITLE} from {self.start_node}")

        plt.show()
