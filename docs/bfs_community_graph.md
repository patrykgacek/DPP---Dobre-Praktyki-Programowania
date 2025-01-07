# BFS Community Graph

This class provides functionality to create, analyze, and visualize how information spreads through social network.

## Usage

```python
from bfs_community_graph import BfsCommunityGraph

# Create a new instance
graph = BfsCommunityGraph()

# Generate a random community
graph.random_community(num_nodes=5, edge_prob=0.4)

# Run BFS analysis starting from "Person_0"
results = graph.run(start_node="Person_0")

# Visualize the results
graph.draw_compare()
```

## Class Overview

### BfsCommunityGraph

```python
BfsCommunityGraph(graph: Graph = None, start_node: str = None, debug: bool = False)
```

Main class for social network analysis using BFS algorithm.

#### Parameters

- `graph` (networkx.Graph, optional): Initial graph representing the social network
- `start_node` (str, optional): Starting node for BFS traversal
- `debug` (bool, optional): Enable debug logging during BFS algorithm execution

## Methods

### run

```python
def run(start_node: str = None) -> List[Dict[str, int]]
```

Executes the BFS algorithm on the graph.

#### Parameters

- `start_node` (str, optional): Node to start the BFS traversal from

#### Returns

- List of dictionaries containing nodes and their levels in BFS order

### make_graph

```python
def make_graph(nodes: List[str], edges: List[Tuple[str, str]]) -> None
```

Creates a graph from given nodes and edges.

#### Parameters

- `nodes`: List of node names
- `edges`: List of edge tuples (source, target)

### random_community

```python
def random_community(num_nodes: int, edge_prob: float, seed: int = None) -> None
```

Generates a random community graph.

#### Parameters

- `num_nodes`: Number of nodes to generate
- `edge_prob`: Probability of edge creation between nodes
- `seed` (optional): Random seed for reproducibility

### Visualization Methods

#### draw_connections

```python
def draw_connections(
    figsize: Tuple[int, int] = (10, 8),
    node_size: int = 2000,
    node_color: str = "lightblue",
    edge_color: str = "gray"
) -> None
```

Visualizes the social network connections.

#### draw_spread

```python
def draw_spread(
    figsize: Tuple[int, int] = (10, 8),
    node_size: int = 2000,
    edge_color: str = "gray",
    cmap: plt.cm = plt.cm.summer,
    alpha: float = 0.5,
    arrow_style: str = "-|>",
    arrow_size: int = 20
) -> None
```

Visualizes the information spread pattern.

#### draw_compare

```python
def draw_compare(
    figsize: Tuple[int, int] = (20, 8),
    node_size: int = 2000,
    node_color: str = "lightblue",
    edge_color: str = "gray",
    spread_cmap: plt.cm = plt.cm.summer,
    spread_arrow_size: int = 20,
    spread_alpha: float = 0.5,
    spread_arrow_style: str = "-|>"
) -> None
```

Displays both the original network and spread pattern side by side.

## Examples

### Creating a Custom Network

```python
# Create a new graph instance
graph = BfsCommunityGraph()

# Define nodes and edges
nodes = [
    "Patryk",
    "Kasia",
    "Kajetan",
    "Ania",
    "Artur",
    "Karolina",
    "Tomek",
    "Klaudia",
    "Krzysiek",
    "Asia",
]
edges = [
    ("Patryk", "Kasia"),
    ("Patryk", "Kajetan"),
    ("Patryk", "Ania"),
    ("Patryk", "Artur"),
    ("Kasia", "Karolina"),
    ("Kasia", "Tomek"),
    ("Kajetan", "Klaudia"),
    ("Kajetan", "Krzysiek"),
    ("Ania", "Asia"),
    ("Ania", "Krzysiek"),
    ("Artur", "Karolina"),
    ("Artur", "Tomek"),
    ("Karolina", "Klaudia"),
    ("Klaudia", "Krzysiek"),
    ("Krzysiek", "Asia"),
]

# Create the graph
graph.make_graph(nodes, edges)

# Run analysis starting from Patryk
results = graph.run("Patryk")

# Visualize the results
graph.draw_compare()
```

### Analyzing a Random Community

```python
# Create and analyze a random community
graph = BfsCommunityGraph()
graph.random_community(num_nodes=5, edge_prob=0.4, seed=42)
results = graph.run("Person_0")

# Show the spread visualization
graph.draw_spread()
```

## Notes

- The class uses NetworkX for graph operations and Matplotlib for visualization
- Node names should be strings
- It is recommended to ensure that the graph is connected for proper BFS traversal
