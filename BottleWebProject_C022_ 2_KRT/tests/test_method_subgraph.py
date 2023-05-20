import method_subgraph_handler
import unittest

class TestPositiveFindCliquesMethods(unittest.TestCase):
    
    # Positive
    def test_find_cliques__3_size_clique_and_5_size_graph__list_of_1_2_3_in_found_cliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: [5],
            5: [4]
        }
        size = 3
        expected_cliques = [1, 2, 3]
        
        # Act
        num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertIn(expected_cliques, actual_cliques)
        
        
    def test_find_cliques__3_size_clique_and_5_size_graph__num_cliques_equal_1(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: [5],
            5: [4]
        }
        size = 3
        expected_num_cliques = 1
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertEqual(actual_num_cliques, expected_num_cliques)
    
    
    def test_find_cliques__2_size_clique_and_3_size_graph__num_cliques_equal_3(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_num_cliques = 3
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertEqual(actual_num_cliques, expected_num_cliques)
        
        
    def test_find_cliques__2_size_clique_and_3_size_graph__list_of_1_2_in_found_cliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_cliques = [1, 2]
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertIn(expected_cliques, actual_cliques)
        
        
    def test_find_cliques__2_size_clique_and_3_size_graph__list_of_1_3_in_found_cliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_cliques = [1, 3]
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertIn(expected_cliques, actual_cliques)
        
        
    def test_find_cliques__2_size_clique_and_3_size_graph__list_of_2_3_in_found_cliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_cliques = [2, 3]
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertIn(expected_cliques, actual_cliques)
    
    
class TestNegativeFindCliquesMethods(unittest.TestCase):
    
    # Negative
    def test_find_cliques__2_size_clique_and_3_size_graph__list_of_2_1_not_in_found_cliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_cliques = [2, 1]
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertNotIn(expected_cliques, actual_cliques)
        
    
    def test_find_cliques__2_size_clique_and_3_size_graph__num_cliques_not_equal_1(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_num_cliques = 1
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertNotEqual(actual_num_cliques, expected_num_cliques)
        
    
    def test_find_cliques__2_size_clique_and_3_size_graph__num_cliques_not_equal_2(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        size = 2
        expected_num_cliques = 2
        
        # Act
        actual_num_cliques, actual_cliques = method_subgraph_handler.find_cliques(graph, size)
        
        # Assert
        self.assertNotEqual(actual_num_cliques, expected_num_cliques)
    
    
class TestPositiveFindSubcliquesMethods(unittest.TestCase):
        
    # Positive
    def test_find_subcliques__3_size_clique_and_3_size_graph_and_prev_nodes_list_of_1_2_and_nodes_dict_of_3__list_of_1_2_3_in_subcliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1, 2]
        nodes = {3}
        size = 3
        expected_subclique = [1, 2, 3]
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        
        # Assert
        self.assertIn(expected_subclique, actual_subcliques)
        
        
    def test_find_subcliques__3_size_clique_and_3_size_graph_and_prev_nodes_list_of_1_2_and_nodes_dict_of_3__subcliques_count_equal_1(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1, 2]
        nodes = {3}
        size = 3
        expected_subcliques_count = 1
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        
        # Assert
        self.assertEqual(len(actual_subcliques), expected_subcliques_count)
        
        
    def test_find_subcliques__2_size_clique_and_3_size_graph_and_prev_nodes_list_of_1_and_nodes_dict_of_2_3__list_of_1_3_in_subcliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1]
        nodes = {2, 3}
        size = 2
        expected_subcliques = [1, 3]
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
    
         # Assert
        self.assertIn(expected_subcliques, actual_subcliques)
        
        
    def test_find_subcliques__2_size_clique_and_3_size_graph_and_prev_nodes_list_of_1_and_nodes_dict_of_2_3__list_of_1_2_in_subcliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1]
        nodes = {2, 3}
        size = 2
        expected_subcliques = [1, 2]
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        
        # Assert
        self.assertIn(expected_subcliques, actual_subcliques)

        
    def test_find_subcliques__3_size_clique_and_2_size_graph_and_prev_nodes_list_of_1_and_nodes_dict_of_2_3__subcliques_count_equal_2(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1]
        nodes = {2, 3}
        size = 2
        expected_subcliques_count = 2
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        
        # Assert
        self.assertEqual(len(actual_subcliques), expected_subcliques_count)
        
        
class TestNegativeFindSubcliquesMethods(unittest.TestCase):
    # Negative
    def test_find_subcliques__2_size_clique_and_3_size_graph_and_prev_nodes_list_of_1_and_nodes_dict_of_2_3__list_of_2_1_not_in_subcliques(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1]
        nodes = {2, 3}
        size = 2
        expected_subcliques = [2, 1]
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        
        # Assert
        self.assertNotIn(expected_subcliques, actual_subcliques)

        
    def test_find_subcliques__3_size_clique_and_2_size_graph_and_prev_nodes_list_of_1_and_nodes_dict_of_2_3__subcliques_count_not_equal_1(self):
        # Arrange
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        prev_nodes = [1]
        nodes = {2, 3}
        size = 2
        expected_subcliques_count = 1
        
        # Act
        actual_subcliques = list(method_subgraph_handler.find_subcliques(graph, prev_nodes, nodes, size))
        
        # Assert
        self.assertNotEqual(len(actual_subcliques), expected_subcliques_count)
        

if __name__ == '__main__':
    unittest.main()