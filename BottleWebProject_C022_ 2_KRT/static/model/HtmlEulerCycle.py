import base64
import random
import networkx as nx
import io
import matplotlib.pyplot as plt

from bottle import request
from static.model.EulerGraph import EulerGraph


class HtmlEulerCycle:
    """Класс формирующий html страницу для поиска цикла Эйлера"""


    # Метод формирования страницы и выполнение поиска цикла эйлера
    @staticmethod
    def find_euler_cycle_command(vertex_count):
        return HtmlEulerCycle.site_header + HtmlEulerCycle.method_description + \
            HtmlEulerCycle.beginning_body % vertex_count + HtmlEulerCycle.random_form % vertex_count + \
            HtmlEulerCycle.create_result(vertex_count) + \
            HtmlEulerCycle.end_site
    
    # Метод формирования результато поиска цикла эйлера
    @staticmethod
    def create_result(vertex_count):
        checkbox_values = EulerGraph.make_adjacency_matrix_symmetric(HtmlEulerCycle.read_matrix_from_page(vertex_count))

        page = HtmlEulerCycle.find_form % (vertex_count,
                                           HtmlEulerCycle.adjacency_matrix_to_html_table(vertex_count,
                                                                                         checkbox_values))

        existence, euler_cycle = EulerGraph.find_euler_cycle(checkbox_values)

        if existence:
            return page + HtmlEulerCycle.result_form % ('Цикл существует', euler_cycle)
        else:
            return page + HtmlEulerCycle.result_form % ('Цикл отсутствует', euler_cycle)

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
        return checkbox_values

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
