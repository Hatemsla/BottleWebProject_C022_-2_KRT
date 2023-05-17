import numpy as np
from bottle import post, request, route, view


def find_max_degree_vertices(graph, k):
    relat_matrix = np.array(graph)
    A = np.array(graph)

    # вычисление булевой степени матрицы смежности и суммирование с таблицей достижимостей
    for i in range(2, k+1):
        l = np.linalg.matrix_power(relat_matrix.astype(bool), i)
        l = l.astype(int)
        A = np.add(A, l)

    n = len(graph)
    A = A.astype(bool)
    A = A.astype(int)

    print(A)

    max_sum = 0
    for row in A:
        row_sum = max(0, sum(row))
        max_sum = max(max_sum, row_sum)

    for i in range(n):
        if sum(A[i]) == max_sum:
            print(i+1)


find_max_degree_vertices([[0, 1, 1, 0, 0, 1, 1, 0],
                          [1, 0, 1, 0, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1],
                          [1, 0, 1, 0, 1, 0, 0, 0],
                          [1, 0, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0]], 3)


@post('/method_max_con')
@route('/method_max_con')
@view('method_max_con')
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
            subgraph_count=f'{subgraph_count}',
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

