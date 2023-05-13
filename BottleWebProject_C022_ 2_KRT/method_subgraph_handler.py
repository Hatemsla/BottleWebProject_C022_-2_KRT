from datetime import datetime
from bottle import post, request, route, view

graph_count = subgraph_count = 0
prev_graph_count = 0
graph_data = []


def adjacency_matrix_to_graph(adj_matrix):
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


@post('/method_subgraph')
@route('/method_subgraph')
@view('method_subgraph')
def form_handler():
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
        graph_data = []
        for i in range(graph_count):
            ls = []
            for j in range(graph_count):
                ls.append(int(request.forms.get(f"{i}{j}g")))
            graph_data.append(ls)

        graph = adjacency_matrix_to_graph(graph_data)
        num_cliques, cliques = find_cliques(graph, subgraph_count)

        print(f"Number of {subgraph_count}-cliques: {num_cliques}")
        for i, clique in enumerate(cliques):
            print(f"Clique {i+1}: {clique}")

        return dict(
            graph_count=f'{graph_count}',
            subgraph_count=f'{subgraph_count}',
            year=datetime.now().year,
            graph_data=graph_data,
            cliques=cliques,
            num_cliques=num_cliques
        )
    else:
        pass
