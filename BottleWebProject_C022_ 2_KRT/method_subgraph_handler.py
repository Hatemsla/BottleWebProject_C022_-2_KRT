from datetime import datetime
from bottle import post, request, route, view
import re

@post('/method_subgraph')
@route('/method_subgraph')
@view('method_subgraph')
def form_handler():
    graph_count = int(request.forms.get('graph_count'))
    # здесь можно производить нужные действия с переданными данными из формы
    # ...
    return dict(
        title='Method subgraph',
        message=f'{graph_count}',
        year=datetime.now().year,
    )