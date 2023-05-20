import unittest
import sys
sys.path.append( '.' )
from static.model.EulerGraph import EulerGraph


class TestPositiveFindCycleEuler(unittest.TestCase):
    """Unittest класс для правильных тестов"""

    def test_graph_is_euler_1_(self):
        """"""

    def test_2(self):
        """"""

    def test_3(self):
        """"""

    def test_4(self):
        """"""


class TestNegativeFindCycleEuler(unittest.TestCase):
    """Unittest класс для неправильных тестов"""

    def test_graph_is_euler_2_vertexs_graph_is_not_euler(self):
        """Unit тест проверки что граф является Эйлеровым. передаёстся 1 вершина. Ожидаемый результат false"""
        # Arrange
        matrix = [[0, 0], [0, 0]]
        expected_answer = False

        # Act
        actual_answer = EulerGraph.is_eulerian_graph(matrix)

        # Assert
        self.assertIn(expected_answer, actual_answer)

    def test_2(self):
        """"""

    def test_3(self):
        """"""

    def test_4(self):
        """"""


if __name__ == '__main__':
    unittest.main()
