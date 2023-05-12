from datetime import datetime
from tkinter.tix import Form
from bottle import post, request, route, view

graph_count = subgraph_count = 0
prev_graph_count = prev_subgraph_count = 0
graph_data = subgraph_data = []

@post('/method_subgraph')
@route('/method_subgraph')
@view('method_subgraph')
def form_handler():
    global graph_count, subgraph_count, graph_data, subgraph_data, prev_graph_count, prev_subgraph_count
    if request.forms.get("form") == "Send1":
        graph_count = int(request.forms.get('graph_count'))
        subgraph_count = int(request.forms.get('subgraph_count'))

        if graph_count != prev_graph_count:
            graph_data = []
        elif subgraph_count != prev_subgraph_count:
            subgraph_data = []

        prev_graph_count = graph_count
        prev_subgraph_count = subgraph_count

        return dict(
            graph_count=f'{graph_count}',
            subgraph_count = f'{subgraph_count}',
            year=datetime.now().year,
            graph_data=graph_data,
            subgraph_data=subgraph_data
        )
    elif request.forms.get("form") == "Confirm":
        graph_data = subgraph_data = []
        for i in range(graph_count):
            ls = []
            for j in range(graph_count):
                ls.append(int(request.forms.get(f"{i}{j}g")))
            graph_data.append(ls)

        for i in range(subgraph_count):
            ls = []
            for j in range(graph_count):
                ls.append(int(request.forms.get(f"{i}{j}sg")))
            graph_data.append(ls)

        return dict(
            graph_count=f'{graph_count}',
            subgraph_count=f'{subgraph_count}',
            year=datetime.now().year,
            graph_data=graph_data,
            subgraph_data=subgraph_data
        )
    else:
        pass