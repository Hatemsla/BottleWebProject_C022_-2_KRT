import method_subgraph_handler
import unittest

class TestCliqueFunctions(unittest.TestCase):
    
    def test_find_cliques(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        num_cliques, cliques = method_subgraph_handler.find_cliques(graph, size)
        self.assertEqual(num_cliques, 3)
        self.assertIn([1, 2], cliques)
        self.assertIn([1, 3], cliques)
        self.assertIn([2, 3], cliques)
        
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: [5],
            5: [4]
        }
        size = 3
        num_cliques, cliques = method_subgraph_handler.find_cliques(graph, size)
        self.assertEqual(num_cliques, 1)
        self.assertIn([1, 2, 3], cliques)
        self.assertNotIn([4, 5], cliques)
    
    def test_find_subcliques(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1]
        nodes = {2, 3}
        size = 2
        subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        self.assertEqual(len(subcliques), 2)
        self.assertIn([1, 2], subcliques)
        
        prev_nodes = [1, 2]
        nodes = {3}
        size = 3
        subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        self.assertEqual(len(subcliques), 1)
        
        prev_nodes = [1]
        nodes = {2, 3}
        size = 3
        subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        self.assertEqual(len(subcliques), 2)

if __name__ == '__main__':
    unittest.main()