from bottle import post, request, route, view
from static.model.HtmlEulerCycle import HtmlEulerCycle
from datetime import datetime
import random


@post('/method_eulerian_cycle')
@route('/method_eulerian_cycle')
@view('method_eulerian_cycle')
def topic_tarasov():
    return dict(
        year=datetime.now().year,
        new_page=True,
        vertex_count=1,
        matrix=[],
        random=random,
        random_value=False)


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
            matrix=[],
            random=random,
            random_value=False)
    elif request.forms.get("form") == "random":
        return dict(
            year=datetime.now().year,
            vertex_count=vertex_count,
            new_page=False,
            matrix=[],
            random=random,
            random_value=True)
    else:
        return HtmlEulerCycle.find_euler_cycle_command(vertex_count)


@post('/result', method='post')
def cycle_search():
    vertex_count = int(request.forms.getunicode('SHARED_TEXT'))
    return HtmlEulerCycle.find_euler_cycle_command(vertex_count)
