import unittest
import networkx as nx
from src.models.bfs_community_graph import BfsCommunityGraph

class TestBfsCommunityGraph(unittest.TestCase):

  def setUp(self) -> None:
    self.graph = BfsCommunityGraph()

  def test_load_graph(self):
    num_nodes = 10
    edge_prob = 0.2
    valid_g_seed = 9
    invalid_g_seed = 7

    # Should return True if the graph is valid
    G = nx.erdos_renyi_graph(num_nodes, edge_prob, valid_g_seed)
    self.assertTrue(self.graph.load_graph(G))

    # Should return False if the graph is not valid
    G = nx.erdos_renyi_graph(num_nodes, edge_prob, invalid_g_seed)
    self.assertFalse(self.graph.load_graph(G))
