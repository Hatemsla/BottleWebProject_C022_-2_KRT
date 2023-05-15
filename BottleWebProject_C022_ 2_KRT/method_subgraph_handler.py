from datetime import datetime
import random
from bottle import post, request, route, view
import base64
import io
import networkx as nx
import matplotlib.pyplot as plt

graph_count = subgraph_count = 0
prev_graph_count = 0
graph_data = []
image_base64 = ''


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


def get_form_graph_data(graph_count):
    """Функция для получения данных о графе с таблицы смежности"""
    graph_data = []
    for i in range(graph_count):
        ls = []
        for j in range(graph_count):
            ls.append(int(request.forms.get(f"{i}{j}g")))
        graph_data.append(ls)
        
    return graph_data


def calculate_subgraph_count(graph_count, subgraph_count, image_base64):
    """Функция для подсчета количества подграфов в графе заданного пользователем"""
    graph = adjacency_matrix_to_graph(graph_data)
    num_cliques, cliques = find_cliques(graph, subgraph_count)
    cliques.sort(key=lambda x: x[0])

    return dict(
        graph_count=f'{graph_count}',
        subgraph_count=f'{subgraph_count}',
        year=datetime.now().year,
        graph_data=graph_data,
        cliques=cliques,
        num_cliques=num_cliques,
        image_base64=image_base64
    )


def calculate_random_subgraph_count(graph_data, subgraph_count, image_base64):
    """Функция для подсчета количества подграфов в случайно заданном графе"""
    graph = adjacency_matrix_to_graph(graph_data)
    num_cliques, cliques = find_cliques(graph, subgraph_count)
    cliques.sort(key=lambda x: x[0])

    return dict(
        graph_count=f'{graph_count}',
        subgraph_count=f'{subgraph_count}',
        year=datetime.now().year,
        graph_data=graph_data,
        cliques=cliques,
        num_cliques=num_cliques,
        image_base64=image_base64
    )
    

def get_graph_edges(graph_data):
    """Функция для конвертации матрицы смежности в список кортежей"""
    n = len(graph_data)
    edges = []
    for i in range(n):
        for j in range(i, n):
            if graph_data[i][j] == 1:
                edges.append((i+1, j+1))
                
    return edges
    

def get_graph_image(edges):
    """Функция для получения изображения графа"""
    G = nx.Graph()
    G.clear()
    G.add_edges_from(edges)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.clf()
    
    return buf


def get_graph_image64(graph_data):
    """Функция для конвертации изображения графа в формат данных base64"""
    edges = get_graph_edges(graph_data)

    buf = get_graph_image(edges)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
        
    return image_base64


@post('/method_subgraph')
@route('/method_subgraph')
@view('method_subgraph')
def form_handler():
    """Функция обработчик формы на сайта"""
    global graph_count, subgraph_count, graph_data, prev_graph_count, image_base64

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
            num_cliques=-1,
            image_base64=''
        )
    elif request.forms.get("form") == "Confirm":
        graph_data = get_form_graph_data(graph_count)
        
        image_base64 = get_graph_image64(graph_data)
        
        return calculate_subgraph_count(graph_count, subgraph_count, image_base64)
    elif request.forms.get("form") == "Random":
        graph_count = int(request.forms.get('graph_count'))
        subgraph_count = int(request.forms.get('subgraph_count'))

        graph_data = generate_adjacency_matrix(graph_count, 0.6)
        
        image_base64 = get_graph_image64(graph_data)
        
        return calculate_random_subgraph_count(graph_data, subgraph_count, image_base64)
    else:
        pass
