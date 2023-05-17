class EulerGraph:
    """Класс содержащий метод поиска цикла Эйлера"""


    # Функция определения графа как Эйлерова
    @staticmethod
    def is_eulerian_graph(adjacency_matrix):
        num_vertices = len(adjacency_matrix)
        
        # Проверка на количество вершин
        if num_vertices < 4:
            return False

        # Проверяем, все ли вершины имеют четную степень
        for i in range(num_vertices):
            degree = sum(adjacency_matrix[i])
            if degree % 2 != 0:
                return False

        return True

    @staticmethod
    def is_empty_graph(adjacency_matrix):
        for row in adjacency_matrix:
            if any(row):
                return True
        return False

    @staticmethod
    def find_euler_cycle(adjacency_matrix):
        if not EulerGraph.is_eulerian_graph(adjacency_matrix) or not EulerGraph.is_empty_graph(adjacency_matrix):
            return False, []

        cycle = []
        stack = []
        num_vertices = len(adjacency_matrix)
        current_vertex = 0  # Начинаем с вершины 0

        while True:
            for next_vertex in range(num_vertices):
                if adjacency_matrix[current_vertex][next_vertex] == 1:
                    stack.append(current_vertex)
                    adjacency_matrix[current_vertex][next_vertex] = 0
                    adjacency_matrix[next_vertex][current_vertex] = 0
                    current_vertex = next_vertex
                    break
            else:
                cycle.append(current_vertex)
                if len(stack) == 0:
                    break
                current_vertex = stack.pop()

        return True, [x + 1 for x in cycle]


    # Функция сравнения рёбр матрицы между точками
    @staticmethod
    def make_adjacency_matrix_symmetric(adjacency_matrix):
        num_vertices = len(adjacency_matrix)

        for i in range(num_vertices):
            for j in range(i+1, num_vertices):
                if adjacency_matrix[i][j] != adjacency_matrix[j][i]:
                    adjacency_matrix[i][j] = adjacency_matrix[j][i] = max(adjacency_matrix[i][j], adjacency_matrix[j][i])

        return adjacency_matrix

