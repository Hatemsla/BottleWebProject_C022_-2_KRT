"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/method_subgraph')
@view('method_subgraph')
def contact():
    """Renders the method subgraph page."""
    return dict(
        graph_count='0',
        subgraph_count='0',
        year=datetime.now().year,
        graph_data=[],
        cliques=[],
        num_cliques=-1,
        main_graph='',
        subgraphs=[],
        is_valid_graph=False,
        is_subgraph_draw=True,
        is_build_matrix=True
    )


@route('/method_max_connections')
@view('method_max_connections')
def contact():
    """Renders the method max connections page."""
    return dict(
        year=datetime.now().year,
        graph_count='0',
        k_step='0',
        graph_data=[],
        main_graph='',
        is_valid_graph=False,
        res='',
        route_data=[[]]
    )


@route('/method_eulerian_cycle')
@view('method_eulerian_cycle')
def contact():
    """Renders the method eulerian cycle page."""
    return dict(
        title='Method eulerian cycle',
        message='Your method eulerian cycle page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
