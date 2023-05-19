import numpy as np
from bottle import post, request, route, view
from datetime import datetime
import random

vertices = ''

graph_count = k_step = prev_graph_count = 0
graph_data = []
main_graph = ''
route_data = []


def find_max_degree_vertices(graph, k):
    global vertices, route_data
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

    if max_sum > 0:
        vertices = ''
        for i in range(n):
            if sum(route_data[i]) == max_sum:
                vertices += str(i + 1) + ' '
    else:
        vertices = 'точки не связаны'

    return dict(
        year=datetime.now().year,
        graph_count=f'{graph_count}',
        k_step=f'{k_step}',
        graph_data=graph_data,
        main_graph='',
        is_valid_graph=False,
        res=vertices,
        route_data=route_data
    )



# find_max_degree_vertices([[0, 1, 1, 0, 0, 1, 1, 0],
#                           [1, 0, 1, 0, 0, 0, 0, 0],
#                           [1, 1, 0, 0, 0, 1, 1, 0],
#                           [0, 0, 0, 0, 0, 0, 1, 0],
#                           [0, 0, 0, 0, 0, 1, 1, 1],
#                           [1, 0, 1, 0, 1, 0, 0, 0],
#                           [1, 0, 1, 1, 1, 0, 0, 0],
#                           [0, 0, 0, 0, 1, 0, 0, 0]], 3)


def get_form_graph_data(graph_c):
    """Функция для получения данных о графе с таблицы смежности"""
    graph_data = []
    for i in range(graph_c):
        ls = []
        for j in range(graph_c):
            ls.append(int(request.forms.get(f"{i}{j}g")))
        graph_data.append(ls)

    return graph_data


def generate_adjacency_matrix(n, p):
    """
    Функция генерирует матрицу смежности неориентированного графа
    с n вершинами и вероятностью ребра p.
    """
    # Создаем пустую матрицу смежности n x n.
    matrix = [[0 for i in range(n)] for j in range(n)]

    # Заполняем матрицу смежности случайными значениями.
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                matrix[i][j] = 1
                matrix[j][i] = 1

    return matrix


@post('/method_max_connections')
@route('/method_max_connections')
@view('method_max_connections')
def form_handler():
    """Функция обработчик формы на сайта"""
    global graph_count, k_step, graph_data, prev_graph_count, main_graph, vertices, route_data
    route_data = []
    vertices = ''
    if request.forms.get("form") == "Send2":
        graph_count = int(request.forms.get('graph_count'))
        k_step = int(request.forms.get('k_step'))

        if prev_graph_count != graph_count:
            graph_data = []

        prev_graph_count = graph_count

        return dict(
            year=datetime.now().year,
            graph_count=f'{graph_count}',
            k_step=f'{k_step}',
            graph_data=graph_data,
            main_graph='',
            is_valid_graph=False,
            res=vertices,
            route_data=route_data
        )
    elif request.forms.get("form") == "Random2":
        graph_count = int(request.forms.get('graph_count'))
        graph_data = generate_adjacency_matrix(graph_count, 0.6)

        # main_graph = get_graph_image64(graph_data)

        return dict(
            year=datetime.now().year,
            graph_count=f'{graph_count}',
            k_step=f'{k_step}',
            graph_data=graph_data,
            main_graph='',
            is_valid_graph=False,
            res=vertices,
            route_data=route_data
        )
    elif request.forms.get("form") == "Confirm2":

        graph_data = get_form_graph_data(graph_count)

        res = find_max_degree_vertices(graph_data, k_step)
        r_data = "["
        for i in route_data:
            r_data += f'{i}'
        r_data += "]"
        write_file_data(f"{datetime.now()} | k_step= {k_step} "
                        f"| graph_data = {graph_data} | route_data={r_data} | max_con_vertices=[{vertices}]\n")
        return res
    else:
        pass


def write_file_data(data):
    with open('static/data_files/data_max_connections.txt', 'a') as file:
        file.write(data)
