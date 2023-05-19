from bottle import post, request, route, view
from static.model.HtmlEulerCycle import HtmlEulerCycle
from static.model.EulerGraph import EulerGraph
from datetime import datetime
import random

file_path = "data_euler_cycle.tpl.json"


@post('/method_eulerian_cycle')
@route('/method_eulerian_cycle')
@view('method_eulerian_cycle')
def topic_tarasov():
    return dict(
        year=datetime.now().year,
        new_page=True,
        vertex_count=1,
        random=random,
        random_value=False,
        is_result=False,
        graph='',
        matrix='',
        is_old_matrix=False, graph_euler=False, euler_cycle=[])


@post('/euler_graph')
@route('/euler_graph')
@view('method_eulerian_cycle')
def create_matrix():
    vertex_count = int(request.forms.getunicode('VERTEX'))
    if request.forms.get("form") == "matrix":
        return dict(
            year=datetime.now().year,
            new_page=False,
            vertex_count=vertex_count,
            random=random,
            random_value=False,
            is_result=False,
            graph='',
            matrix='',
            is_old_matrix=False, graph_euler=False, euler_cycle=[])

    elif request.forms.get("form") == "random":
        return dict(
            year=datetime.now().year,
            vertex_count=vertex_count,
            new_page=False,
            random=random,
            random_value=True,
            is_result=False,
            graph='',
            matrix='',
            is_old_matrix=False, graph_euler=False, euler_cycle=[])


@post('/euler_graph_result', method='post')
@route('/euler_graph_result', method='post')
@view('method_eulerian_cycle')
def cycle_search():
    vertex_count = int(request.forms.getunicode('VERTEX'))
    matrix = HtmlEulerCycle.read_matrix_from_page(vertex_count)
    graph = HtmlEulerCycle.get_graph_image64(matrix)
    graph_euler, euler_cycle = EulerGraph.find_euler_cycle(matrix[:])
    write_file_data(f"{datetime.now()} | vertex count= {vertex_count} "
                    f"| matrix = {matrix} | is euler graph = {graph_euler} | euler cycle={euler_cycle}\n")
    return dict(
        year=datetime.now().year,
        vertex_count=vertex_count,
        new_page=False,
        graph=graph,
        matrix=matrix,
        random=random,
        random_value=False,
        is_result=True,
        is_old_matrix=True, graph_euler=graph_euler, euler_cycle=euler_cycle)


def write_file_data(data):
    """Запись истории поиска цикла Эйлера в файл"""
    with open('static/data_files/data_eulerian_cycle.py.txt', 'a') as file:
        file.write(data)