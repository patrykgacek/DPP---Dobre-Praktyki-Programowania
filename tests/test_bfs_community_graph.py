import unittest
import networkx as nx
from src.models.bfs_community_graph import BfsCommunityGraph

class TestBfsCommunityGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = BfsCommunityGraph()

    def test_result(self):
        """
        Test the result of the BFS algorithm
        """
        print("Testing result...")
        people = [
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
        connections = [
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
        self.graph.make_graph(people, connections)
        self.graph.run()
        self.assertEqual(self.graph.graph.number_of_nodes(), 10)
        self.assertEqual(self.graph.graph.number_of_edges(), 15)
        self.assertEqual(self.graph.spread_graph.number_of_nodes(), 10)
        self.assertEqual(self.graph.spread_graph.number_of_edges(), 9)
        self.assertEqual(self.graph.spread_graph.degree("Patryk"), 4)

    def test_no_params(self):
        """
        Test if the graph is invalid when no parameters are passed
        """
        print("Testing no params...")
        self.assertFalse(self.graph.is_valid())
        self.assertEqual(self.graph.run(), {})

    def test_invalid_params(self):
        """
        Test if the graph is invalid when invalid parameters are passed
        """
        print("Testing invalid params...")
        non_string_nodes = [1, 2, "3", 4]
        non_string_edges = [(1, 2), (2, "3"), ("3", 4)]
        self.graph.make_graph(non_string_nodes, non_string_edges)
        self.assertFalse(self.graph.is_valid())
        self.assertEqual(self.graph.run(), {})

    def test_invalid_start_node(self):
        """
        Test if the graph is invalid when invalid parameters are passed
        """
        print("Testing invalid start node...")
        nodes = ["1", "2", "3", "4"]
        edges = [("1", "2"), ("2", "3"), ("3", "4")]
        self.graph.make_graph(nodes, edges)
        self.graph.start_node = "5"
        self.assertFalse(self.graph.is_valid())
        self.assertEqual(self.graph.run("5"), {})

    def test_make_graph_from_edges(self):
        """
        Test graph creation from a list of edges
        """
        print("Testing make graph from edges...")
        edges = [("Person_1", "Person_2"), ("Person_2", "Person_3"), ("Person_3", "Person_4")]
        self.graph.make_graph([], edges)
        self.assertEqual(self.graph.graph.number_of_nodes(), 4)  # There should be 4 unique nodes
        self.assertEqual(self.graph.graph.number_of_edges(), 3)  # There should be 3 edges

    def test_graph_string_representation(self):
        """
        Check if the string representation includes correct information
        """
        print("Testing graph string representation...")
        edges = [("Person_1", "Person_2"), ("Person_2", "Person_3")]
        self.graph.make_graph([], edges)
        self.graph.start_node = "Person_1"
        graph_str = str(self.graph)
        self.assertIn("Graph Nodes", graph_str)
        self.assertIn("Graph Edges", graph_str)
        self.assertIn("Deep", graph_str)
        self.assertIn("Spread order", graph_str)
        self.assertIn("Start node", graph_str)

    def test_random_community(self):
        """
        Test the random community graph generation
        """
        print("Testing random community...")
        # Generate a random community graph and check if it has the correct number of nodes
        num_nodes = 5
        edge_prob = 0.4
        self.graph.random_community(num_nodes, edge_prob)

        # Check if the generated graph has the specified number of nodes
        self.assertEqual(len(self.graph.graph.nodes), num_nodes)

        # Check if all nodes are labeled as strings (e.g., "Person_0", "Person_1", ...)
        all_labels_are_strings = all(
            isinstance(node, str) and node.startswith("Person_") for node in self.graph.graph.nodes
        )
        self.assertTrue(all_labels_are_strings)
