import unittest

import sys
import os

# Получение абсолютного пути к текущему скрипту
current_dir = os.path.dirname(os.path.abspath(__file__))

# Получение пути к folder1
folder1_path = os.path.join(current_dir, '..', 'static')

# Добавление пути к folder1 в sys.path
sys.path.append(folder1_path)

from model.EulerGraph import EulerGraph


class TestPositiveFindCycleEuler(unittest.TestCase):
    """Unittest класс для правильных тестов"""

    def test_is_euler_5_vertexes_graph_is_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 5 вершин. Ожидаемый результат true"""
        # Arrange
        matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 0]]
        expected_answer = True

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_is_euler_4_vertexes_graph_is_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 4 вершины. Ожидаемый результат true"""
        # Arrange
        matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
        expected_answer = True

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix) and EulerGraph.is_empty_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_is_euler_9_vertexes_graph_is_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 9 вершины. Ожидаемый результат true"""
        # Arrange
        matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0]]
        expected_answer = True

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix) and EulerGraph.is_empty_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_find_euler_cycle_4_vertexes_true_and_cycle(self):
        """Unit тест проверки что граф является Эйлеровым и поиска цикла. передаёстся 4 вершины. Ожидаемый результат true и цикл"""
        # Arrange
        matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
        expected_answer = True
        expected_cycle = [1, 3, 4, 2, 1]

        # Act
        graph_euler, euler_cycle = EulerGraph.find_euler_cycle(matrix[:])

        # Assert
        self.assertEqual(expected_answer, graph_euler)
        self.assertEqual(expected_cycle, euler_cycle)

    def test_find_euler_cycle_5_vertexes_true_and_cycle(self):
        """Unit тест проверки что граф является Эйлеровым и поиска цикла. передаёстся 5 вершин. Ожидаемый результат true и цикл"""
        # Arrange
        matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 0]]
        expected_answer = True
        expected_cycle = [1, 4, 5, 2, 4, 3, 2, 1]

        # Act
        graph_euler, euler_cycle = EulerGraph.find_euler_cycle(matrix[:])

        # Assert
        self.assertEqual(expected_answer, graph_euler)
        self.assertEqual(expected_cycle, euler_cycle)

    def test_find_euler_cycle_9_vertexes_true_and_cycle(self):
        """Unit тест проверки что граф является Эйлеровым и поиска цикла. передаёстся 9 вершин. Ожидаемый результат true и цикл"""
        # Arrange
        matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0]]
        expected_answer = True
        expected_cycle = [1, 3, 5, 8, 7, 9, 6, 8, 2, 7, 6, 5, 4, 3, 2, 1]

        # Act
        graph_euler, euler_cycle = EulerGraph.find_euler_cycle(matrix[:])

        # Assert
        self.assertEqual(expected_answer, graph_euler)
        self.assertEqual(expected_cycle, euler_cycle)


class TestNegativeFindCycleEuler(unittest.TestCase):
    """Unittest класс для неправильных тестов"""

    def test_graph_is_euler_2_vertexes_graph_is_not_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 1 вершина. Ожидаемый результат false"""
        # Arrange
        matrix = [[0, 0], [0, 0]]
        expected_answer = False

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix) and EulerGraph.is_empty_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_graph_is_euler_10_vertexes_graph_is_not_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 10 вершин. Ожидаемый результат false"""
        # Arrange
        matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        expected_answer = False

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix) and EulerGraph.is_empty_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_graph_is_euler_6_vertexes_graph_is_not_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 6 вершин. Ожидаемый результат false"""
        # Arrange
        matrix = [[0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 0, 1, 0]]
        expected_answer = False

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix) and EulerGraph.is_empty_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_graph_is_euler_6_vertexes_graph_is_not_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 15 вершин. Ожидаемый результат false"""
        # Arrange
        matrix = [[0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1], [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]]
        expected_answer = False

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix) and EulerGraph.is_empty_graph(matrix)

        # Assert
        self.assertEqual(expected_answer, actual_answer)

    def test_4(self):
        """"""


if __name__ == '__main__':
    unittest.main()
