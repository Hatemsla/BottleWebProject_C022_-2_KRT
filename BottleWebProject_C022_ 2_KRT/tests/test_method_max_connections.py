import unittest
import numpy as np


class TestPositiveFindMaxConnectedVertices(unittest.TestCase):

    def test_find_max_connected_vertices_k_1_size_6_1(self):
        k = 1
        matrix = [[0, 1], [0, 0]]

        expected_answer = '1 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_3_size_6_1(self):
        k = 3
        matrix = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0]]

        expected_answer = '1 2 3 4 5 6 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_2_size_6_1(self):
        k = 2
        matrix = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0]]

        expected_answer = '1 2 3 4 5 6 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_2_size_5_1(self):
        k = 2
        matrix = [[0, 0, 0, 1, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]]

        expected_answer = '2 4 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_2_size_6_2(self):
        k = 2
        matrix = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0]]

        expected_answer = '1 2 5 6 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_1_size_2_1(self):
        k = 2
        matrix = [[0, 1], [1, 0]]

        expected_answer = '1 2 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_2_size_20_1(self):
        k = 2
        matrix = [[0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0], [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]]

        expected_answer = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 '
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

class TestNegativeFindMaxConnectedVertices(unittest.TestCase):

    def test_find_max_connected_vertices_k_1_size_2_1(self):
        k = 1
        matrix = [[0, 0], [0, 0]]

        expected_answer = 'точки не связаны'
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_1_size_6_1(self):
        k = 1
        matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

        expected_answer = 'точки не связаны'
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)

    def test_find_max_connected_vertices_k_1_size_20_1(self):
        k = 1
        matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        expected_answer = 'точки не связаны'
        result_answer_vertices, result_answer_way = find_max_degree_vertices(matrix, k)
        self.assertEqual(expected_answer, result_answer_vertices)


if __name__ == '__main__':
    unittest.main()


def find_max_degree_vertices(graph, k):
    relat_matrix = np.array(graph)
    route_data = np.array(graph)

    # вычисление булевой степени матрицы смежности и суммирование с таблицей достижимостей
    for i in range(2, k+1):
        l = np.linalg.matrix_power(relat_matrix.astype(bool), i)
        l = l.astype(int)
        route_data = np.add(route_data, l)

    n = len(graph)
    route_data = route_data.astype(bool)
    route_data = route_data.astype(int)

    max_sum = 0
    for row in route_data:
        row_sum = max(0, sum(row))
        max_sum = max(max_sum, row_sum)

    vertices = ''
    if max_sum > 0:
        for i in range(n):
            if sum(route_data[i]) == max_sum:
                vertices += str(i + 1) + ' '
    else:
        vertices = 'точки не связаны'

    return vertices, route_data
