import base64
import random
import networkx as nx
import io
import matplotlib.pyplot as plt

from bottle import request
from static.model.EulerGraph import EulerGraph


class HtmlEulerCycle:
    """Класс формирующий переменные страницу для поиска цикла Эйлера"""

    # Функция сравнения рёбр матрицы между точками
    @staticmethod
    def make_adjacency_matrix_symmetric(adjacency_matrix):
        num_vertices = len(adjacency_matrix)

        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if adjacency_matrix[i][j] != adjacency_matrix[j][i]:
                    adjacency_matrix[i][j] = adjacency_matrix[j][i] = max(adjacency_matrix[i][j],
                                                                          adjacency_matrix[j][i])

        return adjacency_matrix



    # Метод получения матрицы смежности со страницы HTML
    @staticmethod
    def read_matrix_from_page(vertex_count):
        checkbox_values = []
        for i in range(1, vertex_count + 1):
            row = []
            for j in range(1, vertex_count + 1):
                if i == j:
                    row.append(0)
                    continue
                check_name = f'cell-{i}-{j}'
                if check_name in request.forms:
                    row.append(1)
                else:
                    row.append(0)
            checkbox_values.append(row)
        return HtmlEulerCycle.make_adjacency_matrix_symmetric(checkbox_values)

    @staticmethod
    def get_graph_edges(graph_data):
        """Функция для конвертации матрицы смежности в список кортежей"""
        n = len(graph_data)
        edges = []
        for i in range(n):
            for j in range(i, n):
                if graph_data[i][j] == 1:
                    edges.append((i + 1, j + 1))

        return edges

    @staticmethod
    def get_graph_image(edges):
        """Функция для получения изображения графа"""
        G = nx.Graph()
        G.clear()
        G.add_edges_from(edges)
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color='green')
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_color='white')
        buf = io.BytesIO()
        plt.box(False)
        plt.savefig(buf, format='png')
        plt.clf()

        return buf

    @staticmethod
    def get_graph_image64(graph_data):
        """Функция для конвертации изображения графа в формат данных base64"""
        edges = HtmlEulerCycle.get_graph_edges(graph_data)
        buf = HtmlEulerCycle.get_graph_image(edges)
        buf.seek(0)
        main_graph = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        return main_graph
