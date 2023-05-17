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
main_graph = ''
is_subgraph_draw = True


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
            

def calculate_subgraph_count(graph_count, subgraph_count, main_graph, is_subgraph_draw):
    """Функция для подсчета количества подграфов в графе заданного пользователем"""
    graph = adjacency_matrix_to_graph(graph_data)
    num_cliques, cliques = find_cliques(graph, subgraph_count)
    if is_subgraph_draw:
        subgraphs = get_subgraphs_image64(graph_data, cliques)
    else:
        subgraphs = []
    cliques.sort(key=lambda x: x[0])

    return dict(
        graph_count=f'{graph_count}',
        subgraph_count=f'{subgraph_count}',
        year=datetime.now().year,
        graph_data=graph_data,
        cliques=cliques,
        num_cliques=num_cliques,
        main_graph=main_graph,
        subgraphs=subgraphs,
        is_valid_graph=is_valid_graph(graph_data),
        is_subgraph_draw=is_subgraph_draw
    )


def calculate_random_subgraph_count(graph_data, subgraph_count, main_graph, is_subgraph_draw):
    """Функция для подсчета количества подграфов в случайно заданном графе"""
    graph = adjacency_matrix_to_graph(graph_data)
    num_cliques, cliques = find_cliques(graph, subgraph_count)
    if is_subgraph_draw:
        subgraphs = get_subgraphs_image64(graph_data, cliques)
    else:
        subgraphs = []
    cliques.sort(key=lambda x: x[0])

    return dict(
        graph_count=f'{graph_count}',
        subgraph_count=f'{subgraph_count}',
        year=datetime.now().year,
        graph_data=graph_data,
        cliques=cliques,
        num_cliques=num_cliques,
        main_graph=main_graph,
        subgraphs=subgraphs,
        is_valid_graph=is_valid_graph(graph_data),
        is_subgraph_draw=is_subgraph_draw
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


def get_subgraph_image(edges, subgraph_data):
    """Функция для получения изображения подграфа"""
    G = nx.Graph()
    G.clear()
    G.add_edges_from(edges)
    pos = nx.circular_layout(G)
    node_colors = ['red' if node in subgraph_data else 'green' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos)
    nx.draw(G, pos)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.clf()
    
    return buf
    

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


def get_subgraph_images(edges, cliques):
    """Функция для получения картинок подграфов"""
    G = nx.Graph()
    G.clear()
    G.add_edges_from(edges)
    bufs = []
    
    for clique in cliques:
        edges_to_color = [(u, v) for u, v in G.edges() if u in clique and v in clique]
        pos = nx.circular_layout(G)
        node_colors = ['red' if node in clique else 'green' for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, edgelist=edges_to_color, edge_color='red')  # Установите желаемый цвет для ребер
        nx.draw_networkx_edges(G, pos, edgelist=[edge for edge in G.edges() if edge not in edges_to_color], edge_color='black')  # Рисуем остальные ребра
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_color='white')
        buf = io.BytesIO()
        plt.box(False)
        plt.savefig(buf, format='png')
        bufs.append(buf)
        plt.clf()
    
    return bufs


def get_graph_image64(graph_data):
    """Функция для конвертации изображения графа в формат данных base64"""
    edges = get_graph_edges(graph_data)
    buf = get_graph_image(edges)
    buf.seek(0)
    main_graph = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
        
    return main_graph


def get_subgraphs_image64(graph_data, cliques):
    """Функция для получения картинок сабграфа"""
    subgraph = []
    edges = get_graph_edges(graph_data)
    bufs = get_subgraph_images(edges, cliques)
    for i in range(len(cliques)):
        bufs[i].seek(0)
        subgraph.append(base64.b64encode(bufs[i].read()).decode('utf-8'))
        bufs[i].close()
        
    return subgraph


def is_valid_graph(graph_data):
    """Функция проверяющая правильность таблицы смежности графа"""
    
    for i in range(len(graph_data)):
        for j in range(i + 1, len(graph_data)):
            if graph_data[i][j] != graph_data[j][i]:
                return False
            
    return not all(value == 0 for sublist in graph_data for value in sublist)


@post('/method_subgraph')
@route('/method_subgraph')
@view('method_subgraph')
def form_handler():
    """Функция обработчик формы на сайта"""
    global graph_count, subgraph_count, graph_data, prev_graph_count, main_graph, is_subgraph_draw

    if request.forms.get("form") == "Send1":
        graph_count = int(request.forms.get('graph_count'))
        subgraph_count = int(request.forms.get('subgraph_count'))
        is_subgraph_draw = bool(request.forms.get('is_subgraph_draw'))
        
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
            main_graph='',
            subgraphs=[],
            is_valid_graph=False,
            is_subgraph_draw=True
        )
    elif request.forms.get("form") == "Confirm":
        graph_data = get_form_graph_data(graph_count)
        
        main_graph = get_graph_image64(graph_data)

        return calculate_subgraph_count(graph_count, subgraph_count, main_graph, is_subgraph_draw)
    elif request.forms.get("form") == "Random":
        graph_count = int(request.forms.get('graph_count'))
        subgraph_count = int(request.forms.get('subgraph_count'))
        is_subgraph_draw = bool(request.forms.get('is_subgraph_draw'))

        graph_data = generate_adjacency_matrix(graph_count, 0.6)
        
        main_graph = get_graph_image64(graph_data)
        
        return calculate_random_subgraph_count(graph_data, subgraph_count, main_graph, is_subgraph_draw)
    else:
        pass
