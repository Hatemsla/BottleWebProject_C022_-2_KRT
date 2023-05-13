from datetime import datetime
import random
from bottle import post, request, route, view

graph_count = subgraph_count = 0
prev_graph_count = 0
graph_data = []


def adjacency_matrix_to_graph(adj_matrix):
    """Функция для преоброзования таблицы смежности графа в словарь, где ключи - номера нод, а значения списки соединений"""
    graph = {}
    for i in range(len(adj_matrix)):
        edges = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                edges.append(j+1)
        graph[i+1] = edges
    return graph


def find_cliques(graph, size):
    """Функция для поиска уникальных клик заданного размера в графе."""
    cliques = set()
    nodes = set(graph)
    for start_node in nodes:
        subgraph = nodes.intersection(graph[start_node])
        for clique in find_subcliques(graph, [start_node], subgraph, size):
            cliques.add(tuple(sorted(clique)))
    cliques = [list(clique) for clique in cliques]
    num_cliques = len(cliques)
    return num_cliques, cliques


def find_subcliques(graph, prev_nodes, nodes, size):
    """Функция для поиска подклик заданного размера."""
    if len(prev_nodes) == size:
        yield prev_nodes
    else:
        for node in nodes:
            if all(node in graph[prev_node] for prev_node in prev_nodes):
                for clique in find_subcliques(graph, prev_nodes + [node], nodes.intersection(graph[node]), size):
                    yield clique

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


def calculate_subgraph_count(graph_count, subgraph_count):
    """Функция для подсчета количества подграфов в графе заданного пользователем"""
    graph_data = []
    for i in range(graph_count):
        ls = []
        for j in range(graph_count):
            ls.append(int(request.forms.get(f"{i}{j}g")))
        graph_data.append(ls)

    graph = adjacency_matrix_to_graph(graph_data)
    num_cliques, cliques = find_cliques(graph, subgraph_count)

    return dict(
        graph_count=f'{graph_count}',
        subgraph_count=f'{subgraph_count}',
        year=datetime.now().year,
        graph_data=graph_data,
        cliques=cliques,
        num_cliques=num_cliques
    )


def calculate_random_subgraph_count(graph_data, subgraph_count):
    """Функция для подсчета количества подграфов в случайно заданном графе"""
    graph = adjacency_matrix_to_graph(graph_data)
    num_cliques, cliques = find_cliques(graph, subgraph_count)

    return dict(
        graph_count=f'{graph_count}',
        subgraph_count=f'{subgraph_count}',
        year=datetime.now().year,
        graph_data=graph_data,
        cliques=cliques,
        num_cliques=num_cliques
    )


@post('/method_subgraph')
@route('/method_subgraph')
@view('method_subgraph')
def form_handler():
    """Функция обработчик формы на сайта"""
    global graph_count, subgraph_count, graph_data, prev_graph_count
    if request.forms.get("form") == "Send1":
        graph_count = int(request.forms.get('graph_count'))
        subgraph_count = int(request.forms.get('subgraph_count'))
        
        if prev_graph_count != graph_count:
            graph_data = []     

        prev_graph_count = graph_count

        return dict(
            graph_count=f'{graph_count}',
            subgraph_count = f'{subgraph_count}',
            year=datetime.now().year,
            graph_data=graph_data,
            cliques=[],
            num_cliques=-1
        )
    elif request.forms.get("form") == "Confirm":
        return calculate_subgraph_count(graph_count, subgraph_count)
    elif request.forms.get("form") == "Random":
        graph_count = int(request.forms.get('graph_count'))
        subgraph_count = int(request.forms.get('subgraph_count'))

        graph_data = generate_adjacency_matrix(graph_count, 0.6)
        
        return calculate_random_subgraph_count(graph_data, subgraph_count)
    else:
        pass
